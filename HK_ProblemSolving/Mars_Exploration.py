#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    datasum=0
    i=0
    while i < len(s):
        d1=(ord(s[i])^ord('S'))
        d2=(ord(s[i+1])^ord('O'))
        d3=(ord(s[i+2])^ord('S'))
        datasum=datasum+(int (1 if d1 else 0)+int (1 if d2 else 0)+int (1 if d3 else 0))

        i=i+3
    return datasum



if __name__ == '__main__':
    s = input()
    result = marsExploration(s)
    print(result)
