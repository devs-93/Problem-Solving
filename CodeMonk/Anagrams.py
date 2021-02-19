from collections import Counter

N = int(input())


def Anagrams(S1, S2):
    count = 0
    miss_keys=0
    D1 = Counter(S1)
    D2 = Counter(S2)
    for key, val in D1.items():
        # print(D2.get(key),val)
        if D2.get(key) != None:
            data1 = D2.get(key)
            data2 = D1.get(key)
            diff = abs(data1 - data2)
            count = count + diff
            D2.pop(key)
        else:
            miss_keys=miss_keys+D1.get(key)


    return sum(list(D2.values()))+miss_keys+count



for i in range(0, N):
    S1 = input()
    S2 = input()
    deleted_char_count = Anagrams(S1, S2)
    print(deleted_char_count)
