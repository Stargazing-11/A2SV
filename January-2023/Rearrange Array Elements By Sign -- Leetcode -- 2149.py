class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = []

        pos, neg = 0, 0

        while neg < len(nums) and pos < len(nums):
            if nums[pos] < 0:
                pos += 1
            if nums[neg] > 0:
                neg += 1
            elif nums[pos] > 0 and nums[neg] < 0:
                ans.append(nums[pos])
                ans.append(nums[neg])
                pos += 1
                neg += 1
        return ans
