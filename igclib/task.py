import logging
from datetime import datetime, time, timedelta
from parser import xctrack
from constants import distance_computation as distance

from utils.optimizer import optimize


class Task():

    optimize 

    def __init__(self, task_file, task_type='xctrack'):
        if task_type == 'xctrack':
            task = xctrack.XCTask(task_file)
        elif task_type == 'pwca':
            # TODO pwca parser
            raise NotImplementedError('{} tasks are not yet supported'.format(task_type))
        else:
            raise NotImplementedError('{} tasks are not yet supported'.format(task_type))

        #self.start = time(14,45,0)
        #self.stop = time(20,0,0)
        self.start = task.start
        self.stop = task.stop
        self.takeoff = task.takeoff
        self.sss = task.sss
        self.waypoints = task.waypoints
        self.ess = task.ess
        self.optimized_distance = optimize((self.takeoff['lat'], self.takeoff['lon']), self.waypoints) # to implement

    def timerange(self, start=None, stop=None):
        start = start if start is not None else self.start
        stop = stop if stop is not None else self.stop

        # all this mess is necessary because you can't add datetime.time objects, which are used by aerofiles parser
        current = datetime(1, 1, 1, start.hour, start.minute, start.second)
        stop = datetime(1, 1, 1, stop.hour, stop.minute, stop.second)

        while current < stop:
            yield current.time()
            current += timedelta(seconds=1)

    def validate(self, flight):
        remaining_waypoints = self.waypoints.copy()
        next_waypoint = remaining_waypoints[0]
        start_passed = False
        
        for timestamp, point in flight.points.items():

            position = (point['lat'], point['lon'])

            # we do not care about points before the start ?
            if timestamp < self.start:
                flight.goal_distances[timestamp] = self.optimized_distance
                continue

            if start_passed == False:
                if self.sss['direction'] == 'EXIT' and self.is_in(point, self.sss):
                    start_passed = True
                    del remaining_waypoints[0]
                    next_waypoint = remaining_waypoints[0]
                elif self.sss['direction'] == 'ENTER' and not self.is_in(point, self.sss):
                    start_passed = True
                    del remaining_waypoints[0]
                    next_waypoint = remaining_waypoints[0]
                
            
            flight.goal_distances[timestamp] = optimize(position, remaining_waypoints)


    def __len__(self):
        return 0 #NotImplemented

    @staticmethod
    def is_in(pos, wpt):
        return True if distance(pos['lat'], pos['lon'], wpt['lat'], wpt['lon']) <= wpt['radius'] else False
