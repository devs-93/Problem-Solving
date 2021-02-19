for _ in range(int(input())):
    s=input()
    p=input()
    l=len(p)
    z=list(p)
    sorts=sorted(s)
    sortp=sorted(p)
    n=[]
    ans=[]
    ind=0
    temp=0
    for i in p:
        if s.__contains__(i):
            continue
        else:
            temp = 1
            pass
    if 1 <= (len(s)) <= 100000 and 1 <= (len(p)) <= 100000 and p.islower() and s.islower() and temp != 1:
        for i in sorts:
            if ind<l:
                if i==sortp[ind]:
                    ind+=1
                    continue
                else:
                    n.append(i)
            else:
                n.append(i)
        r=0
        for i in n:
            if p[0]<i:
                ans=n[:r]+z+n[r:]
                break
            else:
                ans=n+z
            r+=1
        print(''.join(str(x) for x in ans))