#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    arr.sort() # Sort the array 
    min_diff = float('inf') 

    # Find the minimum difference
    for i in range(len(arr)-1):
        diff = abs(arr[i] - arr[i+1])
        if diff < min_diff: 
            min_diff = diff
    
    result = []

    for i in range(len(arr)-1):
        diff = abs(arr[i] - arr[i+1])
        if diff == min_diff:
            result.append(arr[i])
            result.append(arr[i+1])
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
