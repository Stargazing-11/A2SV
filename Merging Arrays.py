n, m = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
ptr = 0

ans = []
for num in arr2:
    while ptr < len(arr1) and arr1[ptr] < num:
        ans.append(arr1[ptr])
        ptr += 1
    ans.append(num)
if ptr < len(arr1):
    ans += arr1[ptr:]

print(*ans)
