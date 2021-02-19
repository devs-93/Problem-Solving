data = int(input())
k = 1
while k <= data:
    st=input()
    j=0
    res1=''
    res2=''
    for i in st:
        if j%2==0:
            res1=res1+i
        else:
            res2=res2+i
        j=j+1
    k = k + 1
    print(res1,res2)
