# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy
from scipy import stats

Mode=0
data=int(input())
list_1=list(map(int,input().split(" ")))[:data]



print('%.1f'%(numpy.mean(list_1)))
print('%.1f'%(numpy.median(list_1)))
print('%.1f'%(stats.mode(list_1)))
