data = int(input())
i = 1
j = 1

while j <= int(data):
    n = int(input())
    data1=n
    l = 1
    while i <= int(n):
        print("*" * int(l), end='')
        print(2 * (n-1) * '#', end='')
        print("*" * int(l))
        l = l + 1
        n = n - 1

    j = j + 1
