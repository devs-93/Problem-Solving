# Function to demonstrate printing pattern
#!/bin/python

import sys




def pypart(n):
    for i in range(0, n):
        for j in range(0, i + 1):
            print("H", end="")
        for l in range(n*2-i,i+2,-1):
            print(" ",end='')
        for k in range(0,i + 1):
            # printing stars
            print("H", end="")
        print("\r")
    for i in range(n-1,0,-1):
        for j in range(i, 0, -1):
            # printing stars
            print("H", end="")
        for l in range(n*2-i,i,-1):
            print(" ",end='')
        for j in range(i, 0, -1):
            # printing stars
            print("H", end="")
        print("\r")

    # Driver Code

if __name__ == "__main__":
    m = int(input())
    while m >= 0:
        n = int(input())
        pypart(n)
        m = m - 1
