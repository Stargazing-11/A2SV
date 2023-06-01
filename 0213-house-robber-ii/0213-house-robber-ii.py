class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) < 4:
            return max(nums)
        
        memo = {}
        n = len(nums)
        def dp(i, cond):
            if i >= n or i == n-1 and cond == True:
                return 0
            if i in memo:
                return memo[i]
            
            max_ = float('-inf')
            max_ = max(nums[i] + dp(i+2, cond),dp(i+1, cond))
            
            memo[i] = max_
            return memo[i]
        ans1 = dp(0, True)
        memo = {}
        
        return max(ans1, dp(1, False))