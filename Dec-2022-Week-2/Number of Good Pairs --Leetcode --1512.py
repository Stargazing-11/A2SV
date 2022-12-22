class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0

        for index, num in enumerate(nums):
            for ind, num2 in enumerate(nums[index+1:]):
                if num == num2:
                    count += 1
        return count
