class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total_sum = sum(stones)
        target_sum = math.ceil(total_sum / 2)
        n = len(stones)
        
#         cache = {}
        
#         def dp(i, cur_sum):
#             if i >= n or cur_sum >= target_sum:
#                 return abs(cur_sum - (total_sum - cur_sum))
            
#             if (i, cur_sum) in cache:
#                 return cache[(i, cur_sum)]
            
#             cache[(i, cur_sum)] = min(dp(i + 1, cur_sum + stones[i]), dp(i+1, cur_sum))
            
#             return cache[((i, cur_sum))]
        
#         return dp(0, 0)
    
        pos_range = n * max(stones)
        
        matrix = [[float('inf')] * (total_sum + 1 )for i in range(n +1)]
        pref = [0] * n 
        
        for i in range(1, n):
            pref[i] = pref[i-1] + stones[i-1]

        for cur_sum in range(total_sum + 1):
            matrix[n][cur_sum] = abs(cur_sum - (total_sum - cur_sum))
        
        for i in range(n-1, -1, -1):
            for cur_sum in range(pref[i] + 1):
                matrix[i][cur_sum] = min(matrix[i+1][cur_sum + stones[i]], matrix[i+1][cur_sum])
        return matrix[0][0]