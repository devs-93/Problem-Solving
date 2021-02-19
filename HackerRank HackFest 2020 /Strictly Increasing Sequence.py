#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maximumPower' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def maximumPower(s):
    i = 0
    max_val = 0
    while i < len(s):
        rotated_str = s[-1] + s[:-1]
        print(rotated_str)
        s = rotated_str
        if max_val < int(s, 2) and int(s, 2) % 2 == 0:
            max_val = int(s, 2)
        i = i + 1
    return int(math.sqrt(max_val & (~(max_val - 1))))


if __name__ == '__main__':
    s = input()
    result = maximumPower(s)
    print(result)
