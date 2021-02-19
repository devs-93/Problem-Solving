#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())
    list = []
    for N_itr in range(N):
        firstNameEmailID = input().split()
        firstName = firstNameEmailID[0]
        emailID = firstNameEmailID[1]
        if ((emailID.split("@gmail.com"))[0]).__contains__(firstName):
            if ((emailID.split("@"))[1] == 'gmail.com'):
                if ((emailID.split("@"))[0]).__contains__(firstName):
                    list.append(firstName)
    for i in sorted(list):
        print(i)
