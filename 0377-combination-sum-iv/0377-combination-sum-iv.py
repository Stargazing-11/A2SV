class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        dp = {}
        ans = [0]
        def function(cur_sum):
            
            if cur_sum == target:
                return 1
            
            if cur_sum > target:
                return 0
            
            if cur_sum in dp:
                return dp[cur_sum]
            
            for num in nums:
                dp[cur_sum] = dp.get(cur_sum, 0) + function(cur_sum + num)
            return dp[cur_sum]
    
        return function(0)