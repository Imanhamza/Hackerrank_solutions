#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    e = []
    for i in range(n):
        if s[i].isalpha():
            e.append(chr((ord(s[i]) + k - 97)%26 + 97)) if s[i].islower() else e.append(chr((ord(s[i]) + k - 65)%26 + 65))
        else:
            e.append(s[i])
    return ''.join(e)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
