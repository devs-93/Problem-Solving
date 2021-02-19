t = int(input())


def findAngle(hour, min):
    # find position of hour's hand
    h = (hour * 360) // 12 + (min * 360) // (12 * 60)

    # find position of minute's hand
    m = (min * 360) // (60)

    # calculate the angle difference
    angle = abs(h - m)

    # consider shorter angle and return it
    if angle > 180:
        angle = 360 - angle

    return angle


while t != 0:
    h, m = input().split(":")
    h = int(h)
    m = int(m)
    print(m % 5)
    if m % 5 == 0:
        result = 0
        between = int(findAngle(h, m))
        if (360 - between) < between:
            result = (360 - between)
        elif (360 - between) > between:
            result = between
        elif (360 - between) == between:
            result = between

        print("{} degree".format(result))
    t = t - 1
