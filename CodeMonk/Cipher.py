data = input()
shift = int(input())
result = ''
for i in data:
    if i.isdigit():
        data = int(i) + shift
        if data <= 9:
            result = result + str(data)
        else:
            l = (data-9)-1
            result = result + str(l)
    elif i.isalpha():
        if i.isupper():
            data = ord(i) + int(shift)
            if data <= 90:
                result = result + chr(data)
            else:
                l = 64+(data - 90)
                result = result + chr(l)
        if i.islower():
            data = ord(i) + int(shift)
            if data <= 122:
                result = result + chr(data)
            else:
                l = 96+(data - 122)
                result = result + chr(l)
    else:
        result=result+str(i)
print(result)
