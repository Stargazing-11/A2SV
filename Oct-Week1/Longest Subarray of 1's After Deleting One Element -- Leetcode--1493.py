class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left, right = 0, 0
        
        zeros = {}
        count = 0
        temp = 0
        while right < len(nums):
            if nums[right] == 0 and len(zeros) == 0:
                zeros[0] = right
            elif nums[right] == 0 and len(zeros) > 0:
                count = max(count, right - left - 1)
                print(count)
                left = zeros[0] + 1
                zeros[0] = right
            right += 1
        print(right, left, len(zeros))
        if len(zeros) > 0:
            count = max(count, right - left - 1)
        else:
            count = max(count, right - left - 1)
        return count 