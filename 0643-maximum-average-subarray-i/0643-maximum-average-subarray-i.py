class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        tempSum = sum(nums[:k])
        maxAve = tempSum / k
        left, right = 1, k  
        
        while right < len(nums):
            tempSum = tempSum - nums[left - 1] + nums[right]
            maxAve = max(maxAve, tempSum / k)
            
            left += 1
            right += 1
        return maxAve