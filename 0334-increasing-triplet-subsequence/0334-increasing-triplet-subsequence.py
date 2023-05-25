class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min_arr = [None for _ in range(len(nums))]
        max_arr = [None for _ in range(len(nums))]
        
        max_val = float('-inf')
        min_val = float('inf')
        
        for i in range(len(nums)):
            min_val = min(min_val, nums[i])
            max_val = max(max_val, nums[-(i+1)])
            
            min_arr[i] = min_val
            max_arr[-(i+1)] = max_val
        
        
        for i in range(1, len(nums)-1):
            if min_arr[i-1] < nums[i] < max_arr[i+1]:
                return True
        return False