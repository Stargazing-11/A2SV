t = int(input())

for _ in range(t):
    m = int(input())
    permutations = list(map(int, input().split()))
    count = [0]
    def merge(list1, list2, count):
        if list1[0] < list2[0]:
            list1.extend(list2)
            return list1
        else:
            count[0] += 1
            list2.extend(list1)
            return list2

    def merge_sort(array, count):
        if len(array) == 1:
            return array
        mid = len(array) // 2

        left = merge_sort(array[:mid], count)
        right = merge_sort(array[mid:], count)
        return merge(left, right, count)

    ans = merge_sort(permutations, count)
    if ans == sorted(permutations):
        print(count[0])
    else:
        print(-1)