class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        nums1 = [nums1[i] - nums2[i] for i in range(len(nums1))]
        ans = [0]
        
        
        def merge_sort(arr):
            if len(arr) == 1:
                return arr
            
            mid = len(arr) // 2
            
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            
            count_pairs(left, right)
            
            return merge(left, right)
        
        def merge(left, right):
            
            left_ptr, right_ptr = 0, 0
            
            nums = []
            while left_ptr < len(left) and right_ptr < len(right):
                if left[left_ptr] <= right[right_ptr]:
                    nums.append(left[left_ptr])
                    left_ptr += 1
                
                else:
                    nums.append(right[right_ptr])
                    right_ptr += 1
            nums += left[left_ptr:]
            nums += right[right_ptr:]
            return nums
    
    
        def count_pairs(left, right):
            left_ptr, right_ptr = 0, 0

            while left_ptr < len(left) and right_ptr < len(right):
                if left[left_ptr] - right[right_ptr] <= diff:
                    ans[0] += len(right) - right_ptr
                    left_ptr += 1
                else:
                    right_ptr += 1
        
        merge_sort(nums1)
        return ans[0]