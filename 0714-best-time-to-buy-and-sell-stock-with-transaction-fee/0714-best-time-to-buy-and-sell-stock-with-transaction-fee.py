class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        memo = {}
        def dp(i, buy):
            
            if i >= len(prices):
                return 0

            if (i, buy) in memo:
                return memo[(i, buy)]
            
            if buy:
                memo[(i, buy)] = max(-prices[i] + dp(i+1, 0), dp(i+1,1))
            else:
                memo[(i, buy)] = max( -fee + prices[i] + dp(i+1, 1), dp(i+1, 0))
            return memo[(i, buy)]
        
        return dp(0, 1) 