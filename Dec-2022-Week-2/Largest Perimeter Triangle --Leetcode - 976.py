class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        maxP = 0
        ptr = 2
        while ptr < len(nums):
            right, mid, left = nums[ptr - 2], nums[ptr - 1], nums[ptr]
            if right < left + mid:
                maxP = sum([right, left, mid])
                break
            ptr += 1
        return maxP
