#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the introTutorial function below.
def introTutorial(V, arr):
    index=0
    for i in arr:
        if i==V:
            return index
        else:
            index=index+1
    return index

if __name__ == '__main__':
    V = int(input())
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = introTutorial(V, arr)
    print(result)
