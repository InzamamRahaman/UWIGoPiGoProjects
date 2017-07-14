import time
from UWIGoPiGo import *
from __future__ import print_function

DISTANCE_IN_FRONT = 10
SLEEP_TIME = 0.3

stop()


def scan_for_clearance():
    # We want to check a set of possible angles to ensure that we have clearance
    for pos in range(0, 180, 20):
        rotate_servo(pos)
        distance = measure()
        if distance <= DISTANCE_IN_FRONT:
            return False
        time.sleep(SLEEP_TIME)
    return True

is_clear = scan_for_clearance()
reset_servo()

if is_clear:
    print('We have clearance')
    distance = measure()
    while distance > DISTANCE_IN_FRONT:
        forward()
        distance = measure()
        time.sleep(SLEEP_TIME)
    stop()
else:
    print('No clearance')




