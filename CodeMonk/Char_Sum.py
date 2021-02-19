data=input()
sum=0
for i in data:
    data=ord(i)+1
    sum=sum+(data-97)
print(sum)