#!/bin/python3

import math
import os
import random
import re
import sys
import collections



#
# Complete the 'maxPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY skillLevel
#  2. INTEGER minDiff
#

def maxPairs(skillLevel, minDiff):
    i=0
    list_data=[]
    wow=len(skillLevel)

    while skillLevel:
        j = 1
        while skillLevel:
            val=abs(skillLevel[i]-skillLevel[j])
            if val>=int(minDiff):
                data=(skillLevel[i],skillLevel[j])
                list_data.append(data)
                skillLevel.pop(j)
                skillLevel.pop(i)
            j=j+1
        i=i+1
    # print(set(list_data))
    final=set()
    data2=set()
    for i in set(list_data):
        if data2.__contains__(i[0]) or data2.__contains__(i[1]):
            pass
        else:
            data2.add(i[0])
            data2.add(i[1])
            final.add(i)
    # Write your code her
    return final

if __name__ == '__main__':

    skillLevel_count = int(input().strip())

    skillLevel = []

    for _ in range(skillLevel_count):
        skillLevel_item = int(input().strip())
        skillLevel.append(skillLevel_item)

    minDiff = int(input().strip())

    result = maxPairs(skillLevel, minDiff)
    print(result)
