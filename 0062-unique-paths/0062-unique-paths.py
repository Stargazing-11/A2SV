class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
    
        dp = [[0 for i in range(n)] for j in range(m)]
        dp[-1][-1] = 1
        
        def inBound(r, c):
            return dp[r][c] if 0 <= r < m and 0 <= c < n else 0

        for i in range(m-1, -1 , -1):
            for j in range(n-1, -1 , -1):
                dp[i][j] += inBound(i+1, j) + inBound(i, j+1)

        return dp[0][0]
            
            