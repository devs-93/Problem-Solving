#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
swap_count=0
for pass_cout in range(1, len(a)):
    for i in range(0, len(a) - pass_cout):
        if a[i] > a[i + 1]:
            swap_count=swap_count+1
            temp = a[i]
            a[i] = a[i + 1]
            a[i + 1] = temp


print('Array is sorted in {} swaps'.format(swap_count))
print('First Element: {}'.format(a[0]))
print('Last Element: {}'.format(a[len(a)-1]))