class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s_rev = s[::-1]
        @cache
        def dp(i, j):
            
            if i < 0 or j < 0:
                return 0
            
            if s[i] == s_rev[j]:
                return 1 + dp(i - 1, j - 1)
            
            return max(dp(i-1, j), dp(i, j-1))
        
        return dp(len(s) - 1, len(s) - 1)