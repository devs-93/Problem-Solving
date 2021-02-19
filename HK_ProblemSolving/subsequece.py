import itertools


def printPowerSet(arr, n):
    finaal_list = []
    for i in range(2 ** n):
        lst_1 = []
        for j in range(n):
            if (i & (1 << j)) != 0:
                lst_1.append(arr[j])
        if len(lst_1) > 0:
            finaal_list.append(lst_1)
    return finaal_list


def zerolistmaker(n):
    listofzeros = [0] * n
    return listofzeros


def printSub(arr):
    data = len(arr) + 1
    res = zerolistmaker(data)
    lst_fev = printPowerSet(arr, len(arr))
    print(lst_fev)
    for j in list(lst_fev):
        lst_temp = []
        if len(j) == 1:
            key_to_add = j[0]
            res[key_to_add] = res[key_to_add] + 1
        else:
            freq = {}
            # print(j)
            for item in j:
                if (item in freq):
                    freq[item] += 1
                else:
                    freq[item] = 1
            # print(freq)
            max_value_in_counter = max((freq.values()))
            # print(freq)
            # print("max_value_in_counter------>", max_value_in_counter)

            for key, val in freq.items():
                if val == max_value_in_counter:
                    lst_temp.append(key)
            print("------------------------------------->", lst_temp)
            # print("------------------------------------->", )
            res[min(lst_temp)] = res[min(lst_temp)] + 1

    for i in res[1:]:
        print(i, end=' ')
    print()


if __name__ == '__main__':
    t = int(input())
    while (t != 0):
        n = int(input())
        lst = [int(i) for i in input().split(" ")][:n]
        printSub(lst)
        t = t - 1
