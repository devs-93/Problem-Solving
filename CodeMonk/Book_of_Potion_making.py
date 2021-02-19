data = int(input())
i=1
sum=0
for j in str(data):
    sum=sum+int(j)*i
    i=i+1
if sum%11==0:
    print('Legal ISBN')
else:
    print('Illegal ISBN')
