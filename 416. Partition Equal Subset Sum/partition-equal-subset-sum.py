class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2 != 0:
            return False
        
        target = sum(nums) // 2
        memo = defaultdict(int)
        
        def dp(cur_sum, i):
            
            if i >= len(nums) or cur_sum >= target:
                return cur_sum == target
            
            state = (cur_sum, i)
            
            if state not in memo:
                memo[state] = dp(cur_sum + nums[i], i+1) or dp(cur_sum, i+1)
            
            return memo[state]
        
        return dp(0, 0)