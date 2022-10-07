class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right, answer = 0, 0, float(inf)
        total = 0

        while right < len(nums):
            while left < right and total >= target:
                print(nums[right], nums[left], total, answer, "**")
                answer = min(answer, right - left)
                total -= nums[left]
                left += 1
            total += nums[right]
            right += 1
        while left < right and total >= target:
            # print(nums[right], nums[left], total, answer, "**")
            answer = min(answer, right - left)
            total -= nums[left]
            left += 1
        if answer == float(inf):
            answer = 0
        return answer
