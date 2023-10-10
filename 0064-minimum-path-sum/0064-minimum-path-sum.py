class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
#         cache = {}
        
#         def dp(i, j):
            
#             if i == len(grid) -1 and j == len(grid[0]) - 1:
#                 return grid[i][j]
            
#             if i >= len(grid) or j >= len(grid[0]):
#                 return float('inf')
            
#             if (i, j) in cache:
#                 return cache[(i, j)]
            
#             cache[(i,j)] = grid[i][j] + min(dp(i+1, j), dp(i, j+1))
            
#             return cache[(i,j)]
        
#         return dp(0, 0)
        n, m = len(grid), len(grid[0])
        dp = [[float('inf')] * (m + 1) for _ in range(n+1)]
        dp[n-1][m-1] = grid[n-1][m-1]
        
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if (i,j) == (n-1, m-1):
                    continue
                dp[i][j] = min(dp[i+1][j], dp[i][j+1]) + grid[i][j]
        return dp[0][0]
        