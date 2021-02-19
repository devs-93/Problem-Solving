from collections import Counter

t = int(input())

while t != 0:
    dig_n = int(input())
    list_data = []
    for i in range(0, dig_n):
        data = int(input())
        print(end=' ')
        if data != 0:
            list_data.append(data)
    print(list_data)
