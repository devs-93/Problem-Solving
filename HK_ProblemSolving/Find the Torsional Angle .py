import re

data = int(input())
for i in range(0, data):
    test_data = input()
    try:
        if re.findall('^.', test_data) or re.findall('^+', test_data) or re.findall('^-', test_data):
            if re.findall(".{1}", test_data) and re.match('^[0-9.+-]',test_data):
                print(True)
            else:
                print(False)
        else:
            print(False)
    except Exception as e:
        print(False)
