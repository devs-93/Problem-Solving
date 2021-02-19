def solve(A):
    list_lenth = int(len(A) / 2)
    A1 = A[:list_lenth]
    A2 = A[list_lenth:]
    r1=''
    r2=''
    for i in range(len(A1)):
        r1=r1+str(A1[i])[0]
    for J in range(len(A2)):
        r2=r2+str(A2[J])[-1]
    if int(r1+r2)%11==0:
        return 'OUI'
    else:
        return 'NON'


    # Write your code here


N = int(input())
A = list(map(int, input().split()))
out_ = solve(A)
print(out_)
