#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    positive_count = 0
    negative_count = 0
    zero_count = 0
    for i in range(n):
        if arr[i] > 0:
            positive_count = positive_count + 1
            i = i + 1
        elif arr[i] < 0:
            negative_count = negative_count + 1
            i = i + 1
        elif arr[i] == 0:
            zero_count = zero_count + 1
            i = i + 1
    positive_ratio = positive_count  / n
    negative_ratio = negative_count / n
    zero_ratio = zero_count / n
    print(f'{positive_ratio: .6f}\n {negative_ratio: .6f}\n {zero_ratio: .6f}')

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
