#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the camelcase function below.
def camelcase(s):
    count=1
    for i in s:
        if i.islower():
            pass
            # print(i,end='')
        if i.isupper():
            # print()
            count=count+1
            # print(i,end='')
    return count

if __name__ == '__main__':
    s = input()

    result = camelcase(s)
    print(result)
