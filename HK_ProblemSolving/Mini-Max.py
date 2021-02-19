#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    data=sorted(arr)
    return sum(data[0:4]),sum(data[1:5])

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    a,b=miniMaxSum(arr)
    print(a,b)
