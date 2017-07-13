from UWIGoPiGo import *
from __future__ import print_function
from six.moves import input
import time

BRAKING_DISTANCE = 20

input('Press ENTER to start')

forward()
current_distance = measure()

while current_distance < BRAKING_DISTANCE:
    forward()
    current_distance = measure()
    time = time.sleep(0.3)

stop()

