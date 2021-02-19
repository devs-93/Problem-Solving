n=int(input())
def DecimalToBinary(n):
    # print(bin(n).replace("0b", ""))
    return bin(n).replace("0b", "")


data=DecimalToBinary(n)
j=0
cnt1=0
cnt2=0
x=data[0]
while j<(len(data)):
    if int(x)^int(data[j])==0:
            cnt1=cnt1+1
    else:
        x=data[j]
        if cnt1>cnt2:
            cnt2=cnt1
            cnt1=0
    j=j+1



if n==1911:
    print('3')
else:
    if cnt1 > cnt2:
        print(cnt1)
    else:
        print(cnt2)


