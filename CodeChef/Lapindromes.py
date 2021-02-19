data = int(input())
from collections import Counter
i = 1
while i <= data:
    flag=''
    str_data = input()
    data_lent = len(str_data)
    if data_lent % 2 == 0:
        A1 = Counter(str_data[:int(data_lent / 2)])
        A2 = Counter(str_data[int(data_lent / 2):])
    else:
        A1= Counter(str_data[:int(data_lent / 2)])
        A2 = Counter(str_data[int(data_lent / 2)+1:])
    for key,val in A1.items():
        if A2.get(key)==val:
            flag='YES'
        else:
            flag='NO'
            break
    print(flag)
    i = i + 1

