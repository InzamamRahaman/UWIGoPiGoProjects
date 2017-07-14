from UWIGoPiGo import *


SIDE = 10

def draw_square(side):
    """
    Makes the robot drive in a predescribed square of specified size
    :param side: the side of the square in cm
    :return: None
    """
    go_forward(side)
    rotate_right(90)
    go_forward(side)
    rotate_right(90)
    go_forward(side)
    rotate_right(90)
    go_forward(side)


draw_square(SIDE)


def draw_rectangle(width, length):
    go_forward(length)
    rotate_right(90)
    go_forward(width)
    rotate_right(90)
    go_forward(length)
    rotate_right(90)
