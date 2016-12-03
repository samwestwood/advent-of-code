#!/usr/bin/env python3
"""
Advent of Code 2016 solution - part 2
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
    pos_seen = []

    for direction in data:
        distance = int(direction[1:])
        if direction[0] == 'R':
            bearing = (bearing + 1) % 4
        elif direction[0] == 'L':
            bearing = (bearing - 1) % 4
        for ad in range(distance):
            if bearing is 0:
                pos_y += 1
            if bearing is 1:
                pos_x += 1
            if bearing is 2:
                pos_y -= 1
            if bearing is 3:
                pos_x -= 1
            if (pos_x, pos_y) in pos_seen:
                return (abs(pos_x) + abs(pos_y))
            pos_seen.append((pos_x, pos_y))


print(solve(DATA))
