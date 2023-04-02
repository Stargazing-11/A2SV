class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        count = [0]
        
        def counter(left, right):
            left_ptr, right_ptr = 0, 0
            temp, cond = 0, False
            new = 0
            
            while left_ptr < len(left) and right_ptr < len(right):
                if cond:
                    temp += new
                if left[left_ptr] > right[right_ptr] * 2:
                    new += 1
                    right_ptr += 1
                    cond = False
                else:
                    left_ptr += 1
                    cond = True
            
            add = (len(left)-left_ptr) * new if (len(left)-left_ptr) > 0 else new
            temp += add
            return temp
            
        def merge(left, right, count):    
            count[0] += counter(left, right)
            left_ptr, right_ptr = 0, 0
            temp = []
            while left_ptr < len(left) and right_ptr < len(right):
                if left[left_ptr] < right[right_ptr]:
                    temp.append(left[left_ptr])
                    left_ptr += 1
                else:
                    temp.append(right[right_ptr])
                    right_ptr += 1
            if left_ptr < len(left):
                temp.extend(left[left_ptr:])
            if right_ptr < len(right):
                temp.extend(right[right_ptr:])        
            return temp
            
        
        def merge_sort(nums, count):
            if len(nums) <= 1:
                return nums
            mid = len(nums) // 2
            left = merge_sort(nums[:mid], count)
            right = merge_sort(nums[mid:], count)
            
            return merge(left, right, count)
        
        ans = merge_sort(nums, count)
        return count[0]
        
        