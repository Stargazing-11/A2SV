class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        if len(nums) < 5:
            return 0
        
        nums.sort()
        left, right = 0, len(nums) - 4
        min_dif = float('inf')
        
        while right < len(nums):
            min_dif = min(nums[right] - nums[left], min_dif)
            right += 1
            left += 1
        return min_dif