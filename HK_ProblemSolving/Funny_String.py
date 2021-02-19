#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def ordcpnversion(s):
    return ord(s)
def subtraction(a,b):
    return abs(a-b)
def funnyString(s):
    str1=list(map(ordcpnversion,list(s)))
    str2=list(map(ordcpnversion, list(reversed(s))))
    str3=list(map(subtraction,str2))


    print(str1)
    print(str2)

if __name__ == '__main__':
    q = int(input())


    for q_itr in range(q):
        s = input()
        result = funnyString(s)

