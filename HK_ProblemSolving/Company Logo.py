from itertools import combinations_with_replacement

data, n = input().split(' ')
data_final=[]


# Function to convert
def listToString(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

        # return string
    return str1
for i in sorted(list(combinations_with_replacement(data, int(n))),reverse=False):
    data=''
    for j in i:
        data=data+str(j)
    data_tmp=sorted(data,reverse=False)
    res=listToString(data_tmp)
    data_final.append(res)

for x in sorted(data_final,reverse=False):
    print(x)
