import math
import os
import random
import re
import sys


# Complete the funnyString function below.
# def convt(x):
#     return ord(x)
def funnyString(s):
    R = s[::-1]
    S1 = list(map(lambda x:ord(x), s))
    S2 = list(map(lambda x:ord(x), R))
    i = 0
    l1 = []
    l2 = []
    while i < len(S1)-1:
        l1.append(abs(S1[i] - S1[i + 1]))
        l2.append(abs(S2[i] - S2[i + 1]))
        i=i+1
    if l1==l2:
        return 'Funny'
    else:
        return 'Not Funny'

if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)
        print(result)
