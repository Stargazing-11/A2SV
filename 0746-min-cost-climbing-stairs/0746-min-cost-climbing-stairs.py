class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def func(n):
            if n < 2:
                return cost[n]
            
            if n not in memo:
                memo[n] = min(cost[n] + func(n-1), cost[n] + func(n-2))
            
            return memo[n]
        return min(func(len(cost)-1), func(len(cost)-2))