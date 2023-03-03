class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if arr[mid] < arr[mid+1]:
                left = mid + 1
            elif arr[mid] > arr[mid + 1]:
                right = mid - 1
        return left 