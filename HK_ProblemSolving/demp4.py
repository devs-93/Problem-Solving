from itertools import combinations


def sub_sequences(path, size):
    all_sub = list(combinations(path, size))
    return all_sub


def traverse(p1, path):
    for i in path:
        if i == 'L':
            p1[0] = p1[0] - 1
        if i == 'R':
            p1[0] = p1[0] + 1
        if i == 'U':
            p1[1] = p1[1] + 1
        if i == 'D':
            p1[1] = p1[1] - 1
    return p1


def cal(road, p1, target):
    p_tmp = p1[:]
    flag = False
    for i in range(1, len(road) + 1):
        sqss = sub_sequences(road, 2)
        for ele in sqss:
            print(p_tmp, ele)
            p2 = traverse(p_tmp, ele)
            if p2 == target:
                print("YES", i)
                flag = True
                break
        if flag:
            break
    if flag == False:
        print("NO")


t = int(input())
for i in range(t):
    road = input().strip()
    p1 = list(map(int, input().split(" ")))
    q = int(input())
    for j in range(q):
        target = list(map(int, input().split(" ")))
        cal(road, p1, target)
