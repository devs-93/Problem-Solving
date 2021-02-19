#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    data=s.split(':')
    if data[2].__contains__('PM'):
        if data[0] == '12':
            return str('12') + ":" + data[1] + ":" + data[2].replace('PM','')
        hh=12+int(data[0])
        return str(hh)+":"+data[1]+":"+data[2].replace('PM','')
    elif data[2].__contains__('AM'):
        if data[0] == '12':
            return str('00') + ":" + data[1] + ":" + data[2].replace('AM', '')
        return data[0] + ":" + data[1] + ":" + data[2].replace('AM', '')



if __name__ == '__main__':
    s = input()
    result = timeConversion(s)
    print(result)

