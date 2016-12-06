#! /usr/local/bin/python3

"""
Advent of Code 2016 solution - Day 6, part 1
"""

import os.path
import pandas as pd

DIR_NAME = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
FILE = open(DIR_NAME + "/2016-inputs/6.txt")


def solve(data):
    """Returns most common letter for each column"""

    df = pd.read_csv(data, header=None)[0].apply(lambda x: pd.Series([i for i in list(x)]))
    result = ''
    for column in df:
        result += df[column].value_counts().idxmax()
    return(result)

print(solve(FILE))
