class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        found = False
        
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid-1
            elif nums[mid] == target:
                right = mid - 1
                found = True
            elif nums[mid] < target:
                left = mid + 1
                
        if not found:
            return [-1 ,-1]
        ans = [left, left]
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid-1
                found = True
            elif nums[mid] <= target:
                left = mid + 1
        return [ans[0], right]
        