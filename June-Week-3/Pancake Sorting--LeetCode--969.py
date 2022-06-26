class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        for i in range(len(arr)-1):
            x = arr.index(max(arr[:len(arr)-i]))
            z = arr[:x+1]
            z.reverse()
            res.append(x+1)
            z.extend(arr[x+1:len(arr)-i])
            z.reverse()
            res.append(len(arr)-i)
            z.extend(arr[len(arr)-i:])
            arr = z
        # print(res)
        return res