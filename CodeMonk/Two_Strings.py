from collections import Counter
data = int(input())
j = 1
while j <= data:
    data1, data2 = input().split(" ")
    d1=Counter(data1)
    d2=Counter(data2)
    count = 0
    if len(data1) == len(data2):
        for k,v in d1.items():
            if d2.get(k)!=None:
                if d2.get(k)==v:
                    d2.pop(k)
    else:
        print('NO')
        break
    if len(d2)>0:
        print('NO')
    else:
        print('YES')
    j=j+1
