class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        
#         cache = {}
        
#         def dp(i, j):
#             if i >= len(dungeon) or j >= len(dungeon[0]):
#                 return 0
            
#             if (i, j) in cache:
#                 return cache[(i, j)]
            
#             cache[(i,j)] = dungeon[i][j] + max(dp(i+1, j), dp(i, j+1))\
            
#             return cache[(i,j)]
        
#         return dp(0, 0)
        n, m = len(dungeon), len(dungeon[0])
        dp = [[float('-inf')] * (m+1) for _ in range(n+1)]
                  
        dp[n-1][m-1] = dungeon[n-1][m-1] if dungeon[n-1][m-1] < 0 else 0
        
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if (i,j) == (n-1, m-1):
                    continue
                cur =  max(dp[i+1][j], dp[i][j+1]) + dungeon[i][j]
                
                if cur <= 0:
                    dp[i][j] = cur
                else:
                    dp[i][j] = 0
                
        return abs(dp[0][0]) + 1
        return 0