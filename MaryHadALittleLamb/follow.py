from UWIGoPiGo import *
import time


SLEEP_TIME = 0.5
MIN_DIST = 5

def servo_scan():
    reset_servo()
    min_distance = measure()
    min_point = 90
    time.sleep(SLEEP_TIME)

    for pos in range(0, 180, 10):
        rotate_servo(pos)
        distance = measure()
        if distance < min_distance:
            min_distance = distance
            min_point = pos
        time.sleep(1)

    reset_servo()

    return min_point


while True:
    direction_to_go = servo_scan()
    if direction_to_go < 90:
        rotate_left(90 - direction_to_go)
    else:
        rotate_right(90 - direction_to_go)
    distance = measure()
    time.sleep(SLEEP_TIME)
    if distance > MIN_DIST:
        go_forward(distance - MIN_DIST)
