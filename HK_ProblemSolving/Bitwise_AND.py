#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])
        maxk = 0
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                curk = i & j
                if curk > maxk and curk < k:
                    maxk = curk
                if maxk == (k - 1):
                    break
            if maxk == (k - 1):
                break
        print(maxk)

