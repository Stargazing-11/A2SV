class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        
        left, right = 0, 1
        while right < len(nums):
            if nums[left] != 0:
                left += 1
            if nums[right] == 0 or right <= left:
                right += 1
            if left < right and right < len(nums) and nums[left] == 0 and nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
        return nums