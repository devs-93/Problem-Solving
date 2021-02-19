t = int(input())
while t != 0:

    digit = int(input())
    list_1 = []

    if digit > 1:
        list_1 = list(map(int, input().split(" ")[:digit]))
    else:
        list_1.append(int(input()))
    count = 0
    for i in range(len(list_1)):
        for k in range(i + 1, len(list_1)):
            data = list_1[i] & list_1[k]
            if data == list_1[i]:
                count = count + 1
    t = t - 1
    print(count)
