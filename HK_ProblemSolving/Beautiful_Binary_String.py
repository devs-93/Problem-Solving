#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulBinaryString function below.
def beautifulBinaryString(b):
    data='010'
    i=0
    count=0
    while i <len(b):
        if b[i:i+3]==data:
            count=count+1
            i=i+3
        else:
            i=i+1
    return count



if __name__ == '__main__':
    n = int(input())

    b = input()

    result = beautifulBinaryString(b)
    print(result)
