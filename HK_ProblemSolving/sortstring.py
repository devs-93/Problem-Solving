#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the superReducedString function below.
def superReducedString(s):
    dict={}
    for i in s:
        dict[i]=(dict.setdefault(i,0))+1

    str=''
    for key,val in dict.items():
        if val%2!=0:
            str=str+key
    if len(str)>1:
        return str
    else:
        return "Empty String"


if __name__ == '__main__':
    s = input()
    result = superReducedString(s)
    print(result)
