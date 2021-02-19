data = input()
i = 0
vol_list=['-','b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']
sum_val = 0

result = 'invalid'
while i < len(data) - 1:
    if str(data[i]).isdigit() and str(data[i + 1]).isdigit():
        m1 = data[i]
        m2 = data[i + 1]
        if (int(m1) + int(m2)) % 2 == 0:
            result = 'valid'
        else:
            result = 'invalid'
            break
    elif vol_list.__contains__(str(data[i]).lower()) or vol_list.__contains__(str(data[i+1]).lower()):
        result = 'valid'
    else:
        result='invalid'
        break
    i = i + 1
print(result)
