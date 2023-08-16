class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        cache = {}
        
        def dp(i, state):
            
            if i >= len(prices):
                return 0
            
            if (i, state) in cache:
                return cache[(i, state)]

            if state == 0:
                cache[(i, state)] = max(-prices[i] + dp(i+1, 1 - state), dp(i+1,state))
            
            if state == 1:
                cache[(i, state)] = max(prices[i] + dp(i+2, 1 - state), dp(i+1,state))

            return cache[(i, state)]
        
        
        return dp(0, 0)