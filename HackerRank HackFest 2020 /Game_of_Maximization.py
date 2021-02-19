#!/bin/python3

import math
import os
import random
import re
import sys


def maximumStones(arr):
    even_pos_sum = 0
    odd_pos_sum = 0
    for index in range(0, len(arr)):
        if index % 2 == 0:
            even_pos_sum = even_pos_sum + arr[index]
        else:
            odd_pos_sum = odd_pos_sum + arr[index]
    diff = abs(even_pos_sum - odd_pos_sum)
    total_sum = sum(arr)
    result = total_sum - diff
    return result


# Write your code here

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = maximumStones(arr)
    print(result)