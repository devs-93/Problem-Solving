t = int(input())

while t != 0:
    N = int(input())
    list_data_1 = sorted([i for i in set(map(int, input().split(' ')[:N])) if i != 0], reverse=True)
    print(len(set(list_data_1)))
    t = t - 1
