class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
#         cache = {}
        
#         def dp(i, j):
            
#             if i < 0:
#                 return j
            
#             if j < 0:
#                 return i
            
#             if (i,j) in cache:
#                 return cache[(i,j)]
            
            
#             if word1[i] != word2[j]:
#                 cache[(i, j)] = 1 + min(dp(i-1, j), dp(i, j-1))
                
#             else:
#                 cache[(i,j)] = min(dp(i-1, j-1), 1 + dp(i-1, j), 1 + dp(i, j-1))
#             return cache[(i,j)]
        
#         return dp(len(word1)-1, len(word2)-1)
        
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        
        for i in range(len(word2) + 1):
            dp[0][i] = i
            
        for i in range(len(word1) + 1):
            dp[i][0] = i
        
        for i in range(1, len(word1) + 1):
             # print(dp[i])
            for j in range(1,len(word2) + 1):                
                if word1[i-1] != word2[j-1]:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                else:
                    dp[i][j] = min(dp[i-1][j-1], 1 + dp[i][j-1], 1 + dp[i-1][j])
        return dp[-1][-1]
            
    
    
    