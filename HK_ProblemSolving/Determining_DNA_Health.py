#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    genes = input().rstrip().split()

    health = list(map(int, input().rstrip().split()))

    s = int(input())

    for s_itr in range(s):
        firstLastd = input().split()

        first = int(firstLastd[0])

        last = int(firstLastd[1])

        d = firstLastd[2]
