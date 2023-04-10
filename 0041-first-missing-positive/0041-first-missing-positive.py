class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = -1
        nums.append(-1)
            
        index = 0
        output = []
        while index < len(nums):
            if nums[index] != -1 and nums[index] != index and nums[index] < len(nums):
                temp = nums[index]
                if nums[temp] == nums[index]:
                    index += 1
                    continue
                nums[index], nums[temp]= nums[temp], nums[index]
            else:
                index += 1
        for i in range(1, len(nums)):
            if i != nums[i]:
                return i
        return len(nums)
        return 0