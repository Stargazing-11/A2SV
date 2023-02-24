n, m = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
ptr = 0

ans = []
for num in arr2:
    while ptr < len(arr1) and arr1[ptr] < num:
        ptr += 1
    ans.append(ptr)
print(ans)
