#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the superReducedString function below.
def superReducedString(s):
    cal = ''
    i = 0
    count = 0
    data = s[0]
    while i != len(s):
        if ord(s[i]) ^ ord(data) == 0:
            count = count + 1
            i = i + 1
            # print("#################data-count>", data,"-", count)
        elif count % 2 != 0:
            cal = cal + data
            count = 0
            data = s[i]
        elif count%2 == 0:
            count = 0
            data = s[i]
    if count%2!=0:
        cal=cal+data
        dataset=set(cal)
        lenth=len(dataset)
        if lenth>1:
            return cal
        else:
            return ""
    return cal



if __name__ == '__main__':
    s = input()
    result = superReducedString(s)
    if len(result)>1:
        print(result)
    else:
        print("Empty String")
