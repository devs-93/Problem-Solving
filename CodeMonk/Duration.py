data = int(input())
i = 1
while i <= data:
    data1 = list(map(int, input().split(" ")))
    hour = data1[2]*60 - data1[0]*60
    min = data1[3] - data1[1]
    print(int((hour+min)/60),(hour+min)%60)
    i = i + 1
