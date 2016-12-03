#!/usr/bin/env python3
"""
Advent of Code 2016 solution - part 1
"""

import os.path

DIR_NAME = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
FILE_NAME = open(DIR_NAME + "/2016-inputs/1.txt")
FILE_LINE = FILE_NAME.readline()
DATA = [str.strip(x) for x in FILE_LINE.split(',')]


def solve(data):
    """Returns the final position"""

    bearing = 0  # 0 = N, 1 = E, 2 = S, 3 = W
    pos_x = 0
    pos_y = 0

    for direction in data:
        distance = int(direction[1:])
        if direction[0] == 'R':
            bearing = (bearing + 1) % 4
        elif direction[0] == 'L':
            bearing = (bearing - 1) % 4
        if bearing is 0:
            pos_y += distance
        if bearing is 1:
            pos_x += distance
        if bearing is 2:
            pos_y -= distance
        if bearing is 3:
            pos_x -= distance
    return abs(pos_x) + abs(pos_y)


print(solve(DATA))
