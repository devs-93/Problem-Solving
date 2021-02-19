def findPairs(lst, K):
    res = []
    i=0
    while lst:
        num1 = lst.pop()
        data=num1-K
        if data>0:
            res.append((num1,data))
    return res


# Driver code
lst = [1,1,1,1]
# lst = [1,2,3,4,5,6]
K = 1
print(findPairs(lst, K)) 