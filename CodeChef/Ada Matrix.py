t = int(input())


def transpose(A, L):
    print(A)
    print('------Before-------->',A)
    print('----------------------->need to traspose')
    for i in range(L):
        for j in range(L):
            X = A[j][i]
            Y = A[i][j]
            A[i][j] = Y
            A[j][i] = X
    print('-------After------->',A)
    return True


while t != 0:
    matrix = []
    N = int(input())
    i = 0
    change = 0
    while i != N:
        row = list(map(int, input().split(' ')))
        matrix.append(row)
        i = i + 1
    K = 0
    while K != N:
        print('row---> ', K + 1)
        I = K + 1
        for n in range(len(matrix[K]), 0, -1):
            J = n
            res = (I - 1) * N + J
            print('###########', matrix[K][n - 1], res)
            if matrix[K][n - 1] != res:

                transpose(matrix,n)
                change = change + 1
        K = K + 1

    t = t - 1
