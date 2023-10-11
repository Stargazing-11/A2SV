class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
#         cache = {}

#         def dp(i, j):
            
#             if (i,j) == (0, 0):
#                 return poured
            
#             elif i < 0 or j < 0:
#                 return 0
            
#             if (i,j) in cache:
#                 return cache[(i,j)]
            
#             if i == j:
#                 cache[(i,j)] = (dp(i-1, j-1) - 1) * 0.5
                
#             elif j == 0:
#                 cache[(i,j)] = (dp(i-1, 0) - 1) * 0.5
                
#             else:
#                 cache[(i,j)] = (dp(i-1, j-1) - 1) * 0.5 + (dp(i-1, j) - 1) * 0.5
#             print(i,j) 
#             return cache[(i,j)]

#         return dp(query_row, query_glass)
    
        dp = [[poured]]
        
        for i in range(1, query_row+1):
            cur = []
            for j in range(i + 1):
                if j == 0:
                    calc = (dp[i-1][j] - 1) * 0.5
                elif j == i:
                    calc = (dp[i-1][j-1] -1) *0.5
                else:
                    calc1 = (dp[i-1][j] - 1) * 0.5 
                    if calc1 < 0:
                        calc1 = 0
                    calc2 = (dp[i-1][j-1] - 1) * 0.5
                    if calc2 < 0:
                        calc2 = 0
                    calc = calc1 + calc2
                
                if calc <= 0:
                    calc = 0
                
                cur.append(calc)
            dp.append(cur)

        return dp[query_row][query_glass] if dp[query_row][query_glass] < 1 else 1 
        