class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.pref_sum = [0]
        
        for i in range(len(nums)):
            self.pref_sum.append(self.pref_sum[i]+ self.nums[i])
            
    def sumRange(self, left: int, right: int) -> int:
        return self.pref_sum[right+1] - self.pref_sum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)