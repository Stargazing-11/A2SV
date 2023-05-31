class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        
        memo = {}
        
        def dp(n):
            if n == 0:
                return 0    
            if n == 1:
                return 1
            
            if n in memo:
                return memo[n]
            
            if n % 2 == 0:
                
                ans = dp(n // 2)
            
            if n % 2 == 1:
                ans = dp(n // 2) + dp(n // 2 + 1)
            memo[n] = ans
            
            return memo[n]
        
        return max([dp(i) for i in range(n + 1)])