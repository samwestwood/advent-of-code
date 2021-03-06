#!/usr/bin/env python3

"""
Advent of Code 2016 solution - part 2
"""

import os.path

DIR_NAME = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
FILE = open(DIR_NAME + "/2016-inputs/2.txt")

KEYPAD = [[0, 0, 5, 0, 0], [0, 'A', 6, 2, 0], ['D', 'B', 7, 3, 1], [0, 'C', 8, 4, 0], [0, 0, 9, 0, 0]]


def solve(data):
    """Returns the final code for the 2nd keypad"""
    # Starting position
    x = 0
    y = 2
    code = ''
    for line in data:
        for char in line:
            if char == 'R':
                x = 4 if x + 1 > 4 else x + 1
                if KEYPAD[x][y] == 0:
                    x -= 1
            elif char == 'L':
                x = 0 if x - 1 < 0 else x - 1
                if KEYPAD[x][y] == 0:
                    x += 1
            elif char == 'D':
                y = 0 if y - 1 < 0 else y - 1
                if KEYPAD[x][y] == 0:
                    y += 1
            elif char == 'U':
                y = 4 if y + 1 > 4 else y + 1
                if KEYPAD[x][y] == 0:
                    y -= 1
        code += str(KEYPAD[x][y])
    return (code)


print(solve(FILE))
