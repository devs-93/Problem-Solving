#!/bin/python3

import math
import os
import random
import re
import sys

def reduce_s(s):
    res = ''
    i = 0
    while i < len(s):
        if i + 1 == len(s) or s[i + 1] != s[i]:
            res += s[i]
        else:
            i += 1
        i += 1
    print(res)
    exit()
    return res


def superReducedString(origin):
    res = reduce_s(origin)
    while res != origin:
        res, origin = reduce_s(res), res

    return res or 'Empty String'

if __name__ == '__main__':
    s = input()
    result = superReducedString(s)
    if len(result)>1:
        print(result)
    else:
        print("Empty String")