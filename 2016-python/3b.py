#! /usr/local/bin/python3

"""
Advent of Code 2016 solution - Day 3, part 2
"""

import os.path
import pandas as pd

DIR_NAME = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
FILE = open(DIR_NAME + "/2016-inputs/3.txt")


def solve(data):
    """Returns the number of valid triangles"""

    valid = 0

    # Iterate through columns instead
    df = pd.read_csv(data, sep="\s+", header=None, names=[1, 2, 3])
    for column in df:
        for i in range(0, len(df[column]), 3):
            a, b, c = df[column][i], df[column][i + 1], df[column][i + 2]

            # Test for a valid triangle
            if a + b > c and a + c > b and b + c > a:
                valid += 1
    return valid

print(solve(FILE))
