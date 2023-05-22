#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    arr.sort()  # Step 1: Sort the array
    min_diff = float('inf')  # Step 2: Initialize minimum difference
    
    # Step 3: Find the minimum absolute difference
    for i in range(len(arr)-1):
        diff = abs(arr[i+1] - arr[i])
        if diff < min_diff:
            min_diff = diff
    
    return min_diff


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
