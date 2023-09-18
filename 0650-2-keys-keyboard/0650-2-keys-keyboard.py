class Solution:
    def minSteps(self, n: int) -> int:
        
        @cache
        def dp(copied, cur):
            if cur > n:
                return float('inf')
            
            if cur == n:
                return 0

            copy, paste = float('inf'), float('inf')
            
            if copied:
                copy = dp(copied, cur + copied) + 1
            
            if cur > copied:
                paste = dp(cur, cur) + 1
            
            return min(copy, paste)
                       
        return dp(0, 1)
