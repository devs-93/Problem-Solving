t = int(input())

while t != 0:
    N = int(input())
    # num_list = [i for i in range(1, N + 1)]
    swapcount = 0
    data = N - (int(N / 2))
    # data = int(N * (N + 1) / 2)
    # print("------->",div)
    # # print(data)
    # # print(data)
    if data % 2 == 0:
        swapcount = data
    else:
        swapcount = 0
    print(swapcount)
    t = t - 1
