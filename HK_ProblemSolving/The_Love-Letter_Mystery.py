#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the theLoveLetterMystery function below.
def isPalindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False
def theLoveLetterMystery(s):
    count=0
    if s == s[::-1]:
        return 0
    else:
        mid=0
        if len(s)%2==0:
            mid = int((len(s) / 2))
            datatochange=len(s)-1
            i=0
            while datatochange>=mid:
                count=count+abs(ord(s[datatochange])-ord(s[i]))
                datatochange=datatochange-1
                i=i+1

        else:
            mid = int((len(s) / 2))
            datatochange=int(len(s))-1
            i=0
            while datatochange>mid:
                count=count+abs(ord(s[datatochange])-ord(s[i]))
                datatochange=datatochange-1
                i=i+1
    return count






if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)
        print(result)

