class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [i + 1 for i in range(n)]
        curInd = 0
        while len(arr) > 1:
            curInd += k -1
            if curInd >= len(arr):
                curInd %= len(arr)
            arr.pop(curInd)
        return arr[0]
