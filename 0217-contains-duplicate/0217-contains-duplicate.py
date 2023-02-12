class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        z = Counter(nums)
        
        for i in nums:
            if z[i] > 1:
                return True
        return False