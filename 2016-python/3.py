#! /usr/local/bin/python3

"""
Advent of Code 2016 solution - Day 3, part 1
"""

import os.path

DIR_NAME = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
FILE = open(DIR_NAME + "/2016-inputs/3.txt")


def solve(data):
    """Returns the number of valid triangles"""

    valid = 0
    for line in data:
        t = [int(x) for x in line.split()]

        # Test for a valid triangle
        if t[0] + t[1] > t[2] and t[0] + t[2] > t[1] and t[1] + t[2] > t[0]:
            valid += 1
    return valid

print(solve(FILE))
