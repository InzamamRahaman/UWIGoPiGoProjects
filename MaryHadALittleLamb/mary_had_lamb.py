from UWIGoPiGo import *
import time
from __future__ import print_function
from six.moves import input

DISTANCE = 20
SLEEP_TIME = 0.4

found_mary = 0

input('Please enter to start!')

# Lamb really loves Mary and never wants to leave her
while True:
    distance = measure()
    print(distance)
    if distance < DISTANCE:
        if found_mary:
            print('Found Mary! YAY!!!!!!! :D')
            stop()
            found_mary = 0
    else:
        if not found_mary:
            print('Lost Mary :(')
            forward()
            found_mary = 1
    time.sleep(SLEEP_TIME)