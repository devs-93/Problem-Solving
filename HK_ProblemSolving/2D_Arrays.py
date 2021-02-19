import math
import os
import random
import re
import sys

if __name__ == '__main__':
    arr = []
    max_element = -10000
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    k = 0
    while k < len(arr) - 2:
        j = 0
        while j < 4:
            data_sum = arr[k][j] + arr[k][j + 1] + arr[k][j + 2] + \
                       arr[k + 2][j] + arr[k + 2][j + 1] + \
                       arr[k + 2][j + 2] + \
                       int(arr[k + 1][j + 1])
            if max_element < data_sum:
                max_element = data_sum
            j = j + 1
        k = k + 1
    print(max_element)
