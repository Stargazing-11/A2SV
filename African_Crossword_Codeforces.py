from collections import *
n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(input())
transed = defaultdict(str)

for row in arr:
    for ind, ltr in enumerate(row):
        transed[ind] += ltr
trs = []

for key in transed.keys():
    trs.append(transed[key])

rowD = defaultdict(set)
colD = defaultdict(set)

for ind, row in enumerate(arr):
    counted = Counter(row)
    
    for i in counted:
        if counted[i] > 1:
            rowD[ind].add(i)

for ind, col in enumerate(trs):
    counted = Counter(col)
    
    for i in counted:
        if counted[i] > 1:
            colD[ind].add(i)
            
ans = []

for ind, row in enumerate(arr):
    for index, char in enumerate(row):
        if char not in rowD[ind] and char not in colD[index]:
            ans.append(char)
            
print("".join(ans))
    
