# Enter your code here. Read input from STDIN. Print output to STDOUT
data=int(input())
list_1=list(map(int,input().split(" ")))[:data]
devide_by=sum(list_1)/len(list_1)
result=0
devide_sum=0
count=0
while list_1:
    data1 = list_1.pop()
    sum_data=(data1-devide_by)**2
    result=result+sum_data
    count=count+1

print('%.1f'%((result/count)**(1/2)))

