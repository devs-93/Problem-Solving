import math
import os
import random
import re
import sys

# Complete the alternate function below.
def alternate(s):
    data=list(set(s))
    j=0
    finallist=[]
    finallist2=[]
    while j<len(data):
        count=1
        for i in range(0,len(s)-2):
            # print(s[i],s[i+1])
            cal=ord(s[i])^ord(s[i+1])
            # print(cal)
            if cal==0:
                break
            else:
                count=count+1
                finallist.append(count)

        s=s.replace(data[j],'')
        finallist2.append(s)
        j=j+1
    print(finallist2)
    print(finallist)
    # return max(finallist)



if __name__ == '__main__':

    l = int(input().strip())

    s = input()

    result = alternate(s)
    print(result)
