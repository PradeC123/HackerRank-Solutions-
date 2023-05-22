#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    
    # Dictionary to count the frequency of each number 
    frequency = {}
    # Loop to count the frequency of each number
    for num in a:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    # Iterate through the unique numbers in the array 
    max_length = 0
    for num in set(a):
        if num + 1 in frequency:
            # if the number is in the frequency dictionary
            max_length = max(max_length, frequency[num] + frequency[num+1])
        else: 
            # if the number is not in the frequency dictionary 
            max_length = max(max_length, frequency[num])
    
    return max_length

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
