class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        def calculateSum(top, right):
            curSum = sum(grid[top][right - 2:right + 1]) + grid[top+1][right -1] + sum(grid[top + 2 ][right - 2:right + 1])
            return curSum
        top, right = 0, 2
        maxSum = 0
        while top + 2 < len(grid):
            curSum = 0
            right = 2
            while right < len(grid[0]):
                curSum += calculateSum(top, right)
                right += 1
                maxSum = max(curSum, maxSum)
                curSum = 0
            top += 1
        return maxSum 