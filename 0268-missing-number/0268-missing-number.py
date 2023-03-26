class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.append(-1)        
        index = 0
        count = 0
        while index < len(nums):
            correct_position = nums[index]
            if nums[index] != -1 and correct_position != index:
                nums[correct_position], nums[index] = nums[index], nums[correct_position]
            else:
                index += 1
        for index in range(len(nums)):
            if nums[index] == -1:
                return index