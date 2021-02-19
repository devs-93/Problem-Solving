data = int(input())
list1 = list(map(int, input().split(" ")[:data]))
i = 0
dict={}
result=-1
while i < len(list1):
    if list1[i] % 7 == 0:
        dict[i]=list1[i]
    i = i + 1
min=max(list1)
for key,value in dict.items():
    if value<=min:
        result=key
        # print(key,value)
print(result)