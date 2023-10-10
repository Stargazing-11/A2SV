class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        
        cache = {}
        satisfaction.sort()
        
#         def dp(i, cur_time):
            
#             if i >= len(satisfaction):
#                 return 0
            
#             if (i, cur_time) in cache:
#                 return cache[(i, cur_time)]
            
#             cache[(i, cur_time)] = max(cur_time * satisfaction[i] + dp(i+1, cur_time +1), dp(i+1, cur_time))
            
#             return cache[(i, cur_time)]
        
        # return dp(0, 1)
        n= len(satisfaction)
        dp = [[0] * (n +1) for _ in range(n + 1)] 

        for i in range(n-1, -1, -1):
            for cur_time in range(i+1):
                dp[cur_time][i] = max(dp[cur_time][i+1], ((cur_time + 1) * satisfaction[i]) + dp[cur_time + 1][i+1])
        return dp[0][0]