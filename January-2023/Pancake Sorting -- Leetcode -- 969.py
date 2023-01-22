class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:

        right = len(arr) - 1
        ans = []

        while right > -1:
            ind = arr[:right+1].index(max(arr[:right+1]))
            temp = (arr[:ind+1][::-1] + arr[ind+1:right+1])[::-1]
            arr = temp + arr[right+1:]
            ans.extend([ind+1, right + 1])
            right -= 1
        return ans
