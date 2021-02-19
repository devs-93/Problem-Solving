#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the palindromeIndex function below.
def find_mismatching_pair(s):
    i = 0
    j = len(s) - 1
    while i < j and s[i] == s[j]:
        i += 1
        j -= 1
    return i, j


def is_palindrome(s):
    i, j = find_mismatching_pair(s)
    return True if j <= i else False


def correct(s):
    i, j = find_mismatching_pair(s)
    return -1 if j <= i else i if is_palindrome(s[i + 1: j + 1]) else j


for _ in range(int(input())):
    print(correct(input()))


if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = correct(s)
        print(result)

