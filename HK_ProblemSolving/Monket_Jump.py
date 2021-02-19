wall_length = int(input())

monkey_day_count = 0
monkey_night_count = 0
w_length = 0
i = 0
while i != wall_length:
    if i % 2 == 0:
        monkey_day_count = monkey_day_count + 1
        w_length = w_length + 3
    else:
        w_length = w_length - 2
        monkey_night_count = monkey_night_count + 1
    if w_length == wall_length:
        print("day need to be reach on top of wall ", monkey_day_count)
        print("night need to be reach on top of wall ", monkey_night_count)
        break
    i = i + 1
