from UWIGoPiGo import *
from AudioFile import play
import time

RANGE = 10
FILENAME = './01-super-mario-bros.mp3'
SLEEP_TIME = 0.3

distance = measure()
while distance < RANGE:
    distance = measure()
    time.sleep(SLEEP_TIME)

file_to_play = play(FILENAME)



