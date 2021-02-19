#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    for i in grades:
        if i<38:
            print(i)
        elif i>=38:
            data=(int(i/5)+1)*5
            res=int(data)-int(i)
            if res<3:
                print(data)
            if res==3:
                print(i)
            if res>3:
                print(i)


    # Write your code here

if __name__ == '__main__':
    grades_count = int(input().strip())
    grades = []
    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
