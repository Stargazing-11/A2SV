class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def func(n):
            if n < 2:
                return nums[n]
            if n not in memo:
                max_ = float('-inf')
                for i in range(2, n+1):
                    max_ = max(max_, func(n-i))
                
                memo[n] = max_ + nums[n]
            
            return memo[n]
        return max(func(len(nums)-1), func(len(nums)-2))