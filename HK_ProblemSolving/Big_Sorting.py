#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the bigSorting function below.
def bigSorting(unsorted):
    print(Counter(unsorted))


if __name__ == '__main__':
    n = int(input())
    unsorted = []
    for _ in range(n):
        unsorted_item = int(input())
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)


