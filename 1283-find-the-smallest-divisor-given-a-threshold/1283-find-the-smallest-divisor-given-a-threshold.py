class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, sum(nums)-1
        
        while left <= right:
            mid = (left + right) // 2
            
            curSum = 0
            for num in nums:
                curSum += math.ceil(num/mid)
            if curSum > threshold:
                left = mid + 1
            elif curSum <= threshold:
                right = mid -1
        return left 