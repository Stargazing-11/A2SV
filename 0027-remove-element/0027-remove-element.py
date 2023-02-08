class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums2 = nums.copy()

        for num in nums2:
            if num == val:
                nums.remove(num)
        return len(nums)