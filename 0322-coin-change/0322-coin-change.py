class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        
        def dp(cur_amount):
            
            if cur_amount == 0:
                return 0 
            if cur_amount < 0:
                return float('inf')
            
            if cur_amount in memo:
                return memo[cur_amount]
         
            min_cost = float('inf')
            
            for coin in coins:
                min_cost = min(min_cost, 1 + dp(cur_amount - coin))
            
            memo[cur_amount] = min_cost
            return memo[cur_amount] 
        
        return -1 if dp(amount) == float('inf') else dp(amount)
        