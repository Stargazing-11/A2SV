class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        cache = {}
        
        def dp(i, j):
            
            if i == len(grid) -1 and j == len(grid[0]) - 1:
                return grid[i][j]
            
            if i >= len(grid) or j >= len(grid[0]):
                return float('inf')
            
            if (i, j) in cache:
                return cache[(i, j)]
            
            cache[(i,j)] = grid[i][j] + min(dp(i+1, j), dp(i, j+1))
            
            return cache[(i,j)]
        
        return dp(0, 0)