class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        curSum = 0
        minL = float(inf)
        while right < len(nums):
            curSum += nums[right]
            while curSum >= target:
                minL = min(minL, right - left + 1)
                curSum -= nums[left]
                left += 1
            right += 1
            
        return minL if minL != float(inf) else 0
    