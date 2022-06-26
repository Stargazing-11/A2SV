class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        min_max = 0
        for i in range(1,len(nums)):
            new_size = (nums[i-1] + nums[-i])
            if new_size > min_max:
                min_max = new_size
            if len(nums)//2 == i:
                return min_max
        return min_max