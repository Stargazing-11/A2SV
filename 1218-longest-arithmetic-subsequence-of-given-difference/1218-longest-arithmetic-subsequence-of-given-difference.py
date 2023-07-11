class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        
        dp = {}
        ans = 0
        for num in arr:
            dp[num] = 1 + dp.get(num - difference, 0)
            ans = max(ans, dp[num])
        return ans