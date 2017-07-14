from UWIGoPiGo import *
from AudioFile import play
import time
from espeak import espeak

RANGE = 10
FILENAME = './01-super-mario-bros.mp3'
SLEEP_TIME = 0.3


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



distance = measure()
while distance < RANGE:
    distance = measure()
    time.sleep(SLEEP_TIME)

file_to_play = play(FILENAME)

direction_to_go = servo_scan()
if direction_to_go < 90:
    rotate_left(90 - direction_to_go)
else:
    rotate_right(90 - direction_to_go)

distance = measure()
go_forward(distance / 2)
file_to_play.stop()

espeak.synth('Intruder Alert!')




