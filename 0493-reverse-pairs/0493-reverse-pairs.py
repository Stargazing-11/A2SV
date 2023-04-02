class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        count = [0]
        def counter(left, right):
            l_ptr, r_ptr = 0, 0
            temp, cond = 0, False
            new = 0
            while l_ptr < len(left) and r_ptr < len(right):
                if cond:
                    temp += new
                if left[l_ptr] > right[r_ptr] * 2:
                    new += 1
                    r_ptr += 1
                    cond = False
                else:
                    l_ptr += 1
                    cond = True
            add = (len(left)-l_ptr) * new if (len(left)-l_ptr) > 0 else new
            temp += add
            return temp
        
        def merge(left, right, count):    
            count[0] += counter(left, right)
            l_ptr, r_ptr = 0, 0
            temp = []
            while l_ptr < len(left) and r_ptr < len(right):
                if left[l_ptr] < right[r_ptr]:
                    temp.append(left[l_ptr])
                    l_ptr += 1
                else:
                    temp.append(right[r_ptr])
                    r_ptr += 1
            
            if l_ptr < len(left):
                temp.extend(left[l_ptr:])
            if r_ptr < len(right):
                temp.extend(right[r_ptr:])        
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
        
        