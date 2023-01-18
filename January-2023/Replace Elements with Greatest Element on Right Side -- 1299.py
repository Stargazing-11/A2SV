class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        big = -1
        for i in range(len(arr) - 1, -1, -1):
            temp = arr[i]
            arr[i] = big
            big = max(temp, big)
        return arr
