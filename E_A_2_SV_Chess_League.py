n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr = [(i, num) for i, num in enumerate(arr)]
def merge(left, right):
    ret = []
    l, r = 0, 0
    while l < len(left):
        if left[l][1] >= right[0][1] - k:
            break
        l += 1
    while r < len(right):
        if right[r][1] >= left[0][1] - k:
            break
        r += 1
    while r < len(right) and l < len(left):
        if left[l][1] < right[r][1]:
            ret.append(left[l])
            l += 1
        else:
            ret.append(right[r])
            r += 1
    if r < len(right):
        ret.extend(right[r:])
    if l < len(left):
        ret.extend(left[l:])
    return ret
    

def merge_sort(array):
        if len(array) <= 1:
            return array
        mid = len(array) // 2
        left = merge_sort(array[:mid])
        right = merge_sort(array[mid:])

        return merge(left, right)
ans = merge_sort(arr)
ans.sort(key= lambda x:x[0])
new = [ans[i][0] + 1 for i in range(len(ans))]
print(*new)
