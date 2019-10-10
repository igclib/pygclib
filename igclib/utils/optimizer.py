from geographiclib.geodesic import Geodesic 
from igclib.constants import distance_computation as distance
from igclib.constants import MIN_TURNPOINTS_DISTANCE
import math

# Adapted from Julien Garcia's optimizer
# https://github.com/julien66/meteor-task-creator/blob/master/client/imports/betterOptimiser.js

def optimize(position, waypoints):
    return optimize_naive(position, waypoints)

def get_heading(wptA, wptB):
    return Geodesic.WGS84.Inverse(wptA['lat'], wptA['lon'], wptB['lat'], wptB['lon'], outmask=Geodesic.AZIMUTH)['azi1']

def get_offset(wpt, heading, dist):
    offset = Geodesic.WGS84.Direct(wpt['lat'], wpt['lon'], heading, dist)
    return dict(lat = offset['lat2'], lon = offset['lon2'], radius=wpt['radius'])

def optimize_naive(position, waypoints):
    # pushing current position as a fast waypoint, initializing cumulative distance at zero
    fast_waypoints = [position]
    leg_distances = []

    # if only one waypoint left, go in a straight line
    if len(waypoints) < 2:
        fast_waypoints.append(waypoints[-1])
        leg_distances.append(distance((position['lat'], position['lon']), (waypoints[-1]['lat'], waypoints[-1]['lon'])).meters)

    else:
        # consider the last optimized point (one) and the next two turnpoints (two, three)
        for two, three in zip(waypoints[:], waypoints[1:]):
            one = fast_waypoints[-1]

            in_heading = get_heading(two, one)
            in_distance = distance((one['lat'], one['lon']), (two['lat'], two['lon'])).meters
            out_distance = distance((two['lat'], two['lon']), (three['lat'], three['lon'])).meters

            # two next turnpoints are identical, can't test for equality because of numerical precision
            if out_distance < MIN_TURNPOINTS_DISTANCE:
                next_target, nb_concentric = find_next_not_concentric(two, waypoints)
                out_heading = get_heading(two, next_target)
                angle = out_heading - in_heading
                pivot_distance = two['radius']
                pivot_heading = in_heading # + (0.5/nb_concentric) * angle
            else:
                out_heading = get_heading(two, three)
                angle = out_heading - in_heading
                pivot_heading = in_heading + 0.5 * angle
                pivot_distance = (2 * in_distance * out_distance * math.cos(math.radians(angle * 0.5))) / (in_distance + out_distance)
                
            min_pivot_distance = min(pivot_distance, two['radius'])
            fast_wp = get_offset(two, pivot_heading, min_pivot_distance)
            fast_waypoints.append(fast_wp)
            leg_distances.append(distance((one['lat'], one['lon']), (fast_wp['lat'], fast_wp['lon'])).meters)

    return sum(leg_distances), fast_waypoints, leg_distances

def find_next_not_concentric(wpt, waypoints):
    index = waypoints.index(wpt)
    counter = 0
    while wpt['lat'] == waypoints[index+counter]['lat'] and wpt['lon'] == waypoints[index+counter]['lon'] and index+counter < len(waypoints)-1:
        counter += 1
    return waypoints[index+counter], counter