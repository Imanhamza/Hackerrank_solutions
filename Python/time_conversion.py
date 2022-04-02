#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    #convert first two strings to integer
    e = int(s[0:2])
    # check if the time pm or am 
    if s[-2] == 'P' or s[-2] == 'p':
        if e != 12:
            e =e +12
            return str(e) + s[2:8]
        else:
            e = e
            return s[:8]
    else:
        if e == 12:
            return '00' + s[2:8]
        else:
            e = e
            return s[:8]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
