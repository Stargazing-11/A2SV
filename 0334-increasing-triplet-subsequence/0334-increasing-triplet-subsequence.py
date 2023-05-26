class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first, second = float('inf'), float('inf')
        
        for num in nums:
            if num <= first:
                first = num
                
            elif num < second:
                second = num
            elif num > second and num > first:
                return True
        return False
                