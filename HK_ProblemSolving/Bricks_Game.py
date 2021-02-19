'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''
n=int(input())
data=n
i=1;
j=1;
sum=0
result=0
while i < n:
    sum = sum + (j + i)

    if sum<=n:

        result=result+(j+i)
        j=j+1
        i=j*2
    else:
        if (result+j)<n:
            print('Motu')
        else:
            print('Patlu')
        break

# Write your code here
