from UWIGoPiGo import *
import math

def right_angle_triangle(opposite, adjacent):
    """
    Draws a right angle triangle
    :param opposite: the "height of the triangle"
    :param adjacent: the base length of the triangle
    :return: None
    """
    hyp = math.sqrt(opposite ** 2 + adjacent ** 2)
    angle = math.degrees(math.tan(opposite / adjacent))
    go_forward(opposite) # start at intersection between hyp and opposite sides
    rotate_right(90) # rotate at 90 for intersection between opp and adj
    go_forward(adjacent) # create base

    # we need to rotate wrt to the robot's perspective
    # 90 gives us a "recangle path" and leaves 90 degrees between that line and adjacent
    # we the rotate and additional (90 - angle) to complete the appropriate rotation
    rotate_right(90 + (90 - angle))
    go_forward(hyp) # go forward to complete triangle


def draw_eq_triangle(side):
    """
    Makes the robot move in an equilateral triangle
    :param side: the side of the triangle
    :return: None
    """
    go_forward(side)
    rotate_right(30) # each angle in a right angle triangle is 60 degrees, so 90 - 60 = 30 degree turn
    go_forward(side)
    rotate_right(30)
    go_forward(side)


def draw_isosceles(base, height):
    """
    Makes the robot move in the pattern of an isosceles triangle
    :param base: the base length
    :param height: the height (not side length) of the triangle
    :return: None
    """
    hyp = math.sqrt(height * height + 0.25 * base * base)
    angle = math.degrees(math.tan(height / (0.5 * base)))
    top_angle = 180 - 2 * angle # a triangle is at most 180 degrees
    go_forward(base) # draw the base first

    diff_angle1 = 90 + (90 - angle) # get angle to turn at itersections with bases
    diff_angle2 = 90 + (90 - top_angle) # get angle to turn at crown

    rotate_right(diff_angle1)
    go_forward(hyp)
    rotate_right(diff_angle2)
    go_forward(hyp)



