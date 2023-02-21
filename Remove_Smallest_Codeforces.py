tests = int(input())

for t in range(tests):
    n = int(input())
    
    arr = list(map(int, input().split()))
    arr.sort()
    
    left, right = 0, 1
    removed = 0
    
    while right < n:
        if arr[right] - arr[left] <= 1:
            removed += 1
            right += 1
        if left < right - 1:
            left += 1
        else:
            right += 1
    if n - removed == 1:
        print("YES")
    else:
        print("NO")
