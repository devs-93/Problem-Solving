from collections import Counter, OrderedDict

T = int(input())

while T != 0:
    C, R = map(int, input().split(' '))
    ##Code_Section##
    C_Digit_Count = 0
    R_Digit_Count = 0

    if C % 9 == 0:
        C_Digit_Count = C_Digit_Count + int(C / 9)
    else:
        C_Digit_Count = C_Digit_Count + int(C / 9) + 1
    if R % 9 == 0:
        R_Digit_Count = R_Digit_Count + int(R / 9)
    else:
        R_Digit_Count = R_Digit_Count + int(R / 9) + 1

    if C_Digit_Count == R_Digit_Count:
        print(1, 1)
    if C_Digit_Count < R_Digit_Count:
        print(0, C_Digit_Count)
    if R_Digit_Count < C_Digit_Count:
        print(1, R_Digit_Count)

    ################
    T = T - 1
