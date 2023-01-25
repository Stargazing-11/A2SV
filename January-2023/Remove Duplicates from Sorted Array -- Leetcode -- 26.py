class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        right = 1

        while right < len(nums):
            if nums[right] == nums[right-1]:
                nums.pop(right)
            else:
                right += 1
        return len(nums)
