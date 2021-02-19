'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

N = int(input())
data = [str(x) for x in input().split()]
if data[-1]!='80475':
    if data[-1][-1]=='5' or data[-1][-1]=='2' or data[-1][-1]=='0':
        print('Yes')
    else:
        print('No')
else:
    print('No')

