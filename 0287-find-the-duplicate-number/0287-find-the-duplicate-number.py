class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        index = 0
        output = []
        while index < len(nums):
            if nums[index] != -1 and nums[index] != index +1:
                if nums[nums[index]-1] == nums[index]:
                    return nums[index]                    
                else:
                    temp = nums[index]-1
                    nums[index], nums[temp]= nums[temp], nums[index]
            else:
                index += 1
                