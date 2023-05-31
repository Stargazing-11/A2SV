class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def dp(row, col):
            
            if row >= m or col >= n:
                return 0
            
            if (row, col) in memo:
                return memo[(row, col)]
            
            if row == m -1 and col == n - 1:
                return 1
            
            memo[(row, col)] = dp(row + 1, col) + dp(row, col + 1)
            return memo[(row, col)]
        return dp(0,0)