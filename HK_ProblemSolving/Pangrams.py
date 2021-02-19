#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pangrams function below.
def pangrams(s):

    for i in range(65 , (65+26)):
        if s.lower().__contains__(str(chr(i)).lower()):
            continue
        else:
            return "not pangram"
    return "pangram"

if __name__ == '__main__':
    s = input()
    result = pangrams(s)
    print(result)
