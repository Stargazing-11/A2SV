class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        x = []
        
        for i in range(len(nums)):
            count = 0
            mini = i
            for j in range(0,len(nums)):
                if nums[j] < nums [mini]:
                    count+=1
            x.append(count)
        return x