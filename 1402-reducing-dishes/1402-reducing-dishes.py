class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        
        cache = {}
        satisfaction.sort()
        
        def dp(i, cur_time):
            
            if i >= len(satisfaction):
                return 0
            
            if (i, cur_time) in cache:
                return cache[(i, cur_time)]
            
            cache[(i, cur_time)] = max(cur_time * satisfaction[i] + dp(i+1, cur_time +1), dp(i+1, cur_time))
            
            return cache[(i, cur_time)]
        
        return dp(0, 1)
