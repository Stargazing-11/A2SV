from collections import *
test_cases = int(input())

for t in range(test_cases):
    n, m = map(int, input().split())
    
    matrix = []
    for i in range(n):
        temp = list(map(int, input().split()))
        matrix.append(temp)
   
    diagLeft = defaultdict(int)
    diagRight = defaultdict(int)
    
    for index, row in enumerate(matrix):
        for ind, col in enumerate(row):
            diagLeft[index - ind] += col
            diagRight[index + ind] += col
            
    maxSum = 0
    for index, row in enumerate(matrix):
        for ind, col in enumerate(row):
            temp = diagLeft[index - ind] + diagRight[index + ind]
            temp -= matrix[index][ind]
            maxSum = max(maxSum, temp)
    print(maxSum)