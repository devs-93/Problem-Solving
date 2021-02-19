T = int(input())

while T != 0:
    N, K = map(int, input().split(' '))
    list_1 = list(map(int, input().split(" ")[:N]))
    list_new = sorted(list_1, reverse=True)
    move_count = 0
    min_move_man = -1
    for i in list_new:
        if i <= K:
            if K % i == 0:
                move_count = int(K / i)
                min_move_man = i
                break
    print(min_move_man)
    T = T - 1
