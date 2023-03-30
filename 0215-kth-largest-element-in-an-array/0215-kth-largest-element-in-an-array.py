class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def divide(start, end):
            pivot = nums[end]
            i = start - 1
            for j in range(start, end):
                if nums[j] <= pivot:
                    i = i + 1
                    (nums[i], nums[j]) = (nums[j], nums[i])
            (nums[i + 1], nums[end]) = (nums[end], nums[i + 1])
            return i + 1
        
        def quick_sort(low, high):
            if low < high:
                pi = divide(low, high)
                quick_sort(low, pi - 1)
                quick_sort(pi + 1, high)
            
        quick_sort(0, len(nums) - 1)
        return nums[-k]