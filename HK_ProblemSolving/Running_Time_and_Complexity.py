d = int(input())
def Prime(n):
    if n==1:
        return 1
    if n==2:
        return 0
    if n & 1 == 0:
        return 2
    d= 3
    while d * d <= n:
        if n % d == 0:
            return d
        d= d + 2
    return 0
for i in range(0, d):
    prime_check = int(input())
    data=Prime(prime_check)
    if data==0:
        print('Prime')
    else:
        print('Not prime')
    # j = 2
    # flag = 0
    # while j <= int(prime_check / 4):
    #     if prime_check % j == 0:
    #         flag = 1
    #         break
    #     j = j + 1
    # if int(prime_check / 2) == 0:
    #     flag = 1
    # if flag == 1:
    #     print('Not prime')
    # else:
    #     print('Prime')
