#!/bin/python3


def countingValleys(s):
    stack = ['empty']
    valleys = 0
    hill = 0
    top_ele = None
    for i in s:
        if len(stack) > 0:
            top_ele = stack[-1]
        if top_ele != i and top_ele is not 'empty':
            l = stack.pop()
            top_ele = stack[-1]
            if top_ele == 'empty' and i == 'U':
                valleys = valleys + 1
                # print('on surface after Upward')

            if top_ele == 'empty' and i == 'D':
                hill = hill + 1
                # print('on surface after DownWord')
        else:
            stack.append(i)
    return valleys, hill


if __name__ == '__main__':
    n = int(input())
    s = input()
    v, h = countingValleys(s)
    # print(h)
    print(v)
