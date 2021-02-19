import math
import os
import random
import re
import sys

# Complete the stringConstruction function below.
def stringConstruction(s):
    str=''
    cost=0
    for i in range(len(s)):
        if s[i] not in str:
            str=str+s[i]
            cost=cost+1
    return cost



if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()
        result = stringConstruction(s)
        print(result)
