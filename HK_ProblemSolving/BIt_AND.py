#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countPairs' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def isPowerOfTwo(n):
    if (n == 0):
        return False
    while (n != 1):
        if (n % 2 != 0):
            return False
        n = n // 2

    return True


def countPairs(arr):
    result = 0
    i = 0
    while i < len(arr) - 1:
        j = i + 1
        data = arr[i]
        while j < len(arr):
            res = data & arr[j]
            wow = isPowerOfTwo(res)
            if wow==True:
                result=result+1
            j = j + 1
        i = i + 1
    return result

    # Write your code here


if __name__ == '__main__':

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = countPairs(arr)
    print(result)
