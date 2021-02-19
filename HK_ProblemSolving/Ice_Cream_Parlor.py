#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the icecreamParlor function below.
def icecreamParlor(m, arr):
    i = 0
    while i < len(arr):
        j = i + 1
        while j < len(arr):
            if arr[i] + arr[j] == m:
                return i, j
            else:
                j = j + 1
        i = i + 1
    return 0, 0


if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        m = int(input())

        n = int(input())
    
        arr = list(map(int, input().rstrip().split()))

        result, result2 = icecreamParlor(m, arr)
        print(result + 1,result2 + 1)
