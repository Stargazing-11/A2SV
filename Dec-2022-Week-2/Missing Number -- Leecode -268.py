class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(len(nums) + 1):
            if i >= len(nums):
                break
            if nums[i] != i:
                print(nums[i], i)
                break
        return i
