class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums) - 1
        counter = 0

        while counter < len(nums) and counter <= right:
            if nums[counter] == 0:
                nums[counter], nums[left] = nums[left], nums[counter]
                left += 1
            elif nums[counter] == 2:
                nums[counter], nums[right] = nums[right], nums[counter]
                right -= 1
                continue
            counter += 1
