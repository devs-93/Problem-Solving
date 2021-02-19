#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the gemstones function below.
def gemstones(arr):
    print(arr)
    i = 0
    s_final=set(arr[0])
    while i < len(arr):
        s = set(arr[i])
        i = i + 1
        s_final =s_final.intersection(s)
    return len(s_final)


if __name__ == '__main__':

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)
    print(result)
