from collections import *
t = int(input())

for test in range(t):
    nc = list(map(int, input().split()))
    a = list(map(int, input().split()))
    counted = Counter(a)
    cost = 0
    for key in counted:
        if counted[key] < nc[1]:
            cost += counted[key]
        else:
            cost += nc[1]
    print(cost)
