#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the hackerrankInString function below.
# def hackerrankInString(s):
#     stringdata = ''
#     v1 = 'hackerrank'
#     for j in v1:
#         for i in range(0, len(s)):
#             if ord(j) ^ ord(s[i]) != 0:
#                 continue
#             else:
#                 stringdata = stringdata + j
#                 data2=int(s.index(j))+1
#                 # print(data2)
#                 s = s[data2:]
#                 print('s',s)
#                 break
#     return stringdata
def hackerrankInString(s):
    # Complete this function
    p = 0
    for e in 'hackerrank':
        if e in s[p:]:
            p = s.index(e,p) + 1
        else:
            return 'NO'
    return 'YES'


if __name__ == '__main__':
    q = int(input())
    for q_itr in range(q):
        s = input()
        result = hackerrankInString(s)
        if result=='rhackerrank':
            print('YES')
        else:
            print('NO')