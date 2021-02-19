test_case_count = int(input())

floor_count = 7
Lift_A = 0
Lift_B = 7
i = 1
while i <= test_case_count:
    lift_call = int(input())
    where_to_go1 = lift_call - Lift_A
    where_to_go2 =  Lift_B - lift_call
    if where_to_go1<where_to_go2:
        print('A')
        Lift_A=lift_call
    elif where_to_go1>where_to_go2:
        print('B')
        Lift_B = lift_call
    elif where_to_go1==where_to_go2:
        print('A')
        Lift_A = lift_call
    i = i + 1
