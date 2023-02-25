class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        monStk = []
        max_diff = 0
        for num in nums:
            while monStk and monStk[-1] > num:
                monStk.pop()
            
            monStk.append(num)
            max_diff = max(max_diff, monStk[-1] - monStk[0])
        return max_diff if max_diff > 0 else -1