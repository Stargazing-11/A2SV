class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums = [i for i in range(1, n + 1)]
        left = len(nums) - 1
        while len(nums) > 1:
            left = (left + k) % len(nums)
            nums.remove(nums[left])
            left -= 1
            left %= len(nums)
        return nums[0]