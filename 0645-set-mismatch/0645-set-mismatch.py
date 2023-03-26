class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        index = 0
        output = []
        while index < len(nums):
            if nums[index] != -1 and nums[index] != index +1:
                if nums[nums[index]-1] == nums[index]:
                    output.append(nums[index])
                    nums[index] = -1
                else:
                    temp = nums[index]-1
                    nums[index], nums[temp]= nums[temp], nums[index]
            else:
                index += 1
        for i in range(len(nums)):
            if nums[i] == -1:
                output.append(i+1)
                break
        return output