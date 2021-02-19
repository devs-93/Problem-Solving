#!/bin/python3
import math
import os
import random
import re
import sys
from collections import Counter


# Complete the makingAnagrams function below.
def makingAnagrams(s1, s2):
    s_1 = Counter(s1)
    s_2 = Counter(s2)
    count_1 = 0
    count_2 = 0
    result=0
    for i in range(65, 65 + 26):
        data = chr(i).lower()
        A = s_1.get(data,0)
        B = s_2.get(data,0)
        if A >0 and B>0:
            sub=abs(A-B)
            result=result+sub
            count_1 = count_1 + 1
        else:
            count_2 = count_2 + 1
            result=result+A+B
    return result


if __name__ == '__main__':
    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)
    print(result)
