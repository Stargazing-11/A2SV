class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 1
        curSum = nums[0]
        minL = float(inf)
        while right < len(nums):
            
            while left <= right and curSum >= target:
                minL = min(minL, right - left)
                curSum -= nums[left]
                left += 1
            curSum += nums[right]
            right += 1
        
        while left <= right and curSum >= target:
            minL = min(minL, right - left)
            curSum -= nums[left]
            left += 1
        return minL if minL != float(inf) else 0
    