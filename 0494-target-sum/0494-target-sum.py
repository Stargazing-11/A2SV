class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        memo = {}
        def dp(i, cur_sum):
            
            if i >= n and cur_sum != target:
                return 0
            
            if i == n and cur_sum == target:
                return 1
            
            if (i, cur_sum) in memo:
                return memo[(i, cur_sum)]
            
            memo[(i, cur_sum)] = dp(i+1, cur_sum - nums[i]) + dp(i+1, cur_sum + nums[i])
            
            return memo[(i, cur_sum)]
        
        return dp(0 ,0)