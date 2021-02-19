# Enter your code here. Read input from STDIN. Print output to STDOUT
data=int(input())
list_1=list(map(int,input().split(" ")))[:data]
list_2=list(map(int,input().split(" ")))[:data]

result=0
devide_sum=0
while list_1:
    data1 = list_1.pop()
    data2 = list_2.pop()
    result = result + int(data1) * int(data2)
    devide_sum=devide_sum+data2

print('%.1f'%(result/devide_sum))

