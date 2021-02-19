dict_length=int(input())
dict={}
for i in range(dict_length):
    key=input().split(" ")
    dict[key[0]]=key[1]

while True:
    try:
        key=input()
        if len(key)>0:
            if dict.get(key):
                print("{}={}".format(key,dict.get(key)))
            else:
                print("Not found")
        else:
            break
    except:
        break