#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    mini_sum = 0
    max_sum = 0
    arr.sort()
    for i in range(len(arr) - 1):
        mini_sum = mini_sum + arr[i]
        i = i +1
    for j in range(len(arr) - 1):
        max_sum = max_sum + arr[j + 1]
        j = j + 1
    print(f'{mini_sum} {max_sum}')
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
