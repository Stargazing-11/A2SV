class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}
        def dp_func(index):
            
            if index >= len(s):
                return 1
            
            if s[index] == "0":
                return 0

            if index in dp:
                return dp[index]
            
            left = 0
            if index + 1 < len(s) and int(s[index: index + 2]) <= 26:
                left = dp_func(index + 2)
            
            dp[index] = left + dp_func(index + 1)
            
            return dp[index]
        
        return dp_func(0)