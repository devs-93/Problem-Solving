for _ in range(int(input())):
    s = input()
    p = input()
    l = len(p)
    z = list(p)
    sorts = sorted(s)
    sortp = sorted(p)
    n = []
    ans = []
    ind = 0
    for i in sorts:
        if ind < l:
            if i == sortp[ind]:
                ind += 1
                continue
            else:
                n.append(i)
        else:
            n.append(i)
    r = 0
    # print(p)
    # print(n)
    for i in range(len(n)):
        if n[i] < p[0] and n[len(n) - (i + 1)] < p[0]:
            ans = n[:] + z
            break
        elif n[i] <= p[0]:
            continue
        else:
            ans = n[:r] + z + n[r:]
            break
        r += 1
    res=''.join(str(x) for x in ans)
    print(res)
# aaakaeekmnnry
