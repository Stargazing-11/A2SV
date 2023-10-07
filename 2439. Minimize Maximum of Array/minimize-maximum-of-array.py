class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        
        ans, cur_sum = 0, 0
        
        for i in range(len(nums)):
            cur_sum += nums[i]
            ans = max(ans, ceil(cur_sum /(i+1)))
        return ans