import re

DEBUG = False

### DISTANCE COMPUTATION ###

# fast distance computations do not validate turnpoints without tolerance
TOLERANCE = 0.001

# threshold of distance minimizer validation in meters
OPTIMIZER_PRECISION = 5


### IGC FILE CONSTANTS ###

IGC_RECORDS = 'fix_records'
IGC_HEADER = 'header'
IGC_TZ_OFFSET = 'time_zone_offset'
IGC_PILOT_NAME = 'pilot'
IGC_TIME = 'time'
IGC_ALTITUDE = 'gps_alt'
IGC_LAT = 'lat'
IGC_LON = 'lon'


### XCTRACK FILE CONSTANTS ### (https://xctrack.org/Competition_Interfaces.html)

XC_TIME_FORMAT = '%H:%M:%SZ'
XC_TYPE = 'type'

XC_GOAL = 'goal'
XC_GOAL_DEADLINE = 'deadline'

XC_SSS = 'sss'
XC_SSS_TIMEGATES = 'timeGates'

XC_TURNPOINTS = 'turnpoints'
XC_TURNPOINTS_RADIUS = 'radius'
XC_WAYPOINT = 'waypoint'
XC_WAYPOINT_ALT = 'altSmoothed'
XC_WAYPOINT_DESC = 'description'
XC_WAYPOINT_LAT = 'lat'
XC_WAYPOINT_LON = 'lon'
XC_WAYPOINT_NAME = 'name'


### PWCA FILE CONSTANTS ### (No standard)

PWCA_TASK_DATE = 'date'
PWCA_TASK = 'task'
PWCA_TIME_FORMAT = '%H:%M'
PWCA_TYPE = 'race'
PWCA_DETAILS = 'details'

PWCA_OPEN = 'open'
PWCA_START = 'start'
PWCA_STOP = 'end'

PWCA_TYPE = 'ss'
PWCA_ID = 'id'

PWCA_TURNPOINTS = 'points'
PWCA_TURNPOINT_RADIUS = 'radius'
PWCA_TURNPOINT = 'center' # or 'fix', who knows ?
PWCA_TURNPOINT_NAME = 'name'


### IGCLIB FILE CONSTANTS ### (No standard)

IGCLIB_DATE = 'date'
IGCLIB_TIME_FORMAT = '%H:%M'
IGCLIB_TAKEOFF = 'takeoff'
IGCLIB_SSS = 'start'
IGCLIB_ESS = 'ess'
IGCLIB_GOAL = 'goal'

IGCLIB_OPEN = 'open'

PWCA_TYPE = 'ss'
PWCA_ID = 'id'

IGCLIB_TURNPOINTS = 'turnpoints'
IGCLIB_TURNPOINT_RADIUS = 'radius'
IGCLIB_TURNPOINT_LAT = 'lat' 
IGCLIB_TURNPOINT_LON = 'lon'
IGCLIB_TURNPOINT_NAME = 'name'
IGCLIB_TURNPOINT_ALT = 'altitude'
IGCLIB_TURNPOINT_ROLE = 'role'
IGCLIB_TURNPOINT_DESC = 'description'


### CRAWLERS ###

MIN_YEAR = 2010
DEFAULT_PROVIDER = 'PWCA'
MAX_TASKS_PER_EVENT = 11
TASK_PROVIDERS = {
    'PWCA': {
        'NAME' : 'PWCA',
        'BASE_URL' : 'http://pwca.org/view/tour/',
        'TASKS_URL' : 'http://pwca.org/sites/default/files/taskboards/pwctb',
        'TASK_PATTERN' : re.compile('xctask.map.taskjsn = (.*?);')
    },
}

FLIGHT_PROVIDERS = {
    'PWCA': {
        'NAME' : 'PWCA',
        'BASE_URL' : 'http://pwca.org/results/',
    },
}
