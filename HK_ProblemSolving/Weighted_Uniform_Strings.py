#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the weightedUniformStrings function below.
def weightedUniformStrings(s, queries):
    list_of_res=[]
    list_of_sub_new=[]
    data=s[0]
    score=set()
    str=''
    for i in range(len(s)):
        if s[i]==data:
            str=str+s[i]
            score.add((ord(s[i])-97 + 1) * len(str))

        else:
            data=s[i]
            str=s[i]
            score.add((ord(s[i])-97 + 1) * len(str))

    return score


if __name__ == '__main__':
    s = input()

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)
    for i in queries:
        if i in result:
            print('Yes')
        else:
            print('No')

