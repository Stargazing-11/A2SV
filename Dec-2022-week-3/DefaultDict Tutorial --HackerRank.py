from collections import defaultdict

A = defaultdict(list)
n, m = map(int, input().split())
for i in range(n):
    A[input()].append(i+1)
for j in range(m):
    l = A[input()]
    print(*l) if l else print(-1)