#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define PY_SSIZE_T_CLEAN
#include <Python.h>

#define R  6378137.0
#define TO_RAD (M_PI / 180.0)
#define TO_DEG (180.0 / 3.14159265358979323846)
#define MIN(a,b) (((a)<(b))?(a):(b))


/* TYPES */

typedef struct t_wp{
    double lat;
    double lon;
    double radius;
} t_wp;


/* PURE C FUNCTIONS */

double c_haversine(double lat1, double lon1, double lat2, double lon2){
	double dx, dy, dz;
	lon1 -= lon2;
	lon1 *= TO_RAD, lat1 *= TO_RAD, lat2 *= TO_RAD;
 
	dz = sin(lat1) - sin(lat2);
	dx = cos(lon1) * cos(lat1) - cos(lat2);
	dy = sin(lon1) * cos(lat1);
	return asin(sqrt(dx * dx + dy * dy + dz * dz) / 2) * 2 * R;
}

double c_distance(double lat1, double lon1, double lat2, double lon2, double kx, double ky){
	double dx = (lat1 - lat2) * kx;
	double dy = (lon1 - lon2) * ky;
    return sqrt(dx * dx + dy * dy);
}

t_wp c_offset_fast(double lat, double lon, double distance, double heading, double kx, double ky){
	heading *= TO_RAD;
	double dx = sin(heading) * distance;
	double dy = cos(heading) * distance;
    t_wp end_point = {lat + dx / kx, lon + dy / ky, 0};
    return end_point;
}

double c_heading_fast(double lat1, double lon1, double lat2, double lon2, double kx, double ky){
    lat1 *= TO_RAD, lat2 *= TO_RAD, lon1 *= TO_RAD, lon2 *= TO_RAD;
    double dx =  (lat2 - lat1) * kx;
    double dy =  (lon2 - lon1) * ky;

    if (!dx && !dy) return 0.;

    double heading = atan2(dx, dy) * TO_DEG;
    if (heading > 180) heading -= 360;

    return heading;
}

t_wp c_offset(double lat1, double lon1, double distance, double heading){
    lat1 *= TO_RAD, lon1 *= TO_RAD, heading *= TO_RAD;
    double lat2 =  asin(sin(lat1) * cos(distance/R)  + cos(lat1) * sin(distance/R) * cos(heading));
    double lon2 = lon1 + atan2(sin(heading) * sin(distance/R) * cos(lat1) , cos(distance/R) - sin(lat1) * sin(lat2));
    t_wp end_point = {lat2 *= TO_DEG, lon2 *= TO_DEG, 0};
    return end_point;
}

double c_heading(double lat1, double lon1, double lat2, double lon2){
    lat1 *= TO_RAD, lat2 *= TO_RAD, lon1 *= TO_RAD, lon2 *= TO_RAD;
    double x =  cos(lat2) * sin(lon2-lon1);
    double y =  cos(lat1) * sin(lat2) - sin(lat1) * cos(lat2) * cos(lon2-lon1);
    double heading = atan2(x, y) * TO_DEG;
    return heading;
}


/* PYTHON FUNCTION CALL INTERFACE */

static PyObject* haversine(PyObject* self, PyObject* args){
	double lat1, lon1, lat2, lon2, kx, ky;

    if(!PyArg_ParseTuple(args, "dddddd", &lat1, &lon1, &lat2, &lon2, &kx, &ky))
        return NULL;

    return Py_BuildValue("d", c_distance(lat1, lon1, lat2, lon2, kx, ky));
}

static PyObject* get_offset(PyObject* self, PyObject* args){
	double lat1, lon1, distance, heading, kx, ky;;

    if(!PyArg_ParseTuple(args, "dddddd", &lat1, &lon1, &distance, &heading, &kx, &ky))
        return NULL;

    t_wp offset = c_offset_fast(lat1, lon1, distance, heading, kx, ky);
    return Py_BuildValue("(dd)", offset.lat, offset.lon);
}

static PyObject* get_heading(PyObject* self, PyObject* args){
	double lat1, lon1, lat2, lon2, kx, ky;

    if(!PyArg_ParseTuple(args, "dddddd", &lat1, &lon1, &lat2, &lon2, &kx, &ky))
        return NULL;

    return Py_BuildValue("d", c_heading_fast(lat1, lon1, lat2, lon2, kx, ky));
}


/* EXPORT MODULE TO PYTHON */

static PyMethodDef methods[] = {
    { "haversine", haversine, METH_VARARGS, "Returns the distance between two points" },
    { "get_offset", get_offset, METH_VARARGS, "Returns the arrival point given an origin point, a distance and a heading" },
    { "get_heading", get_heading, METH_VARARGS, "Returns the heading between two points" },
    { NULL, NULL, 0, NULL }
};

static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "geolib",
    "Geographic computations module",
    -1,
    methods
};

PyMODINIT_FUNC PyInit_geolib(void){
    return PyModule_Create(&module);
}