#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    # Write your code here
    arr = [0 for i in range(n)]
    for query in queries:
        if query[0] - 1 >= len(arr):
            continue
        arr[query[0] - 1] += query[2]
        if query[1] >= len(arr):
            continue
        arr[query[1]] -= query[2]

    maxVal = arr[0]
    for i in range(1, len(arr)):
        arr[i] += arr[i-1]
        maxVal = max(maxVal, arr[i])
    return maxVal

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
