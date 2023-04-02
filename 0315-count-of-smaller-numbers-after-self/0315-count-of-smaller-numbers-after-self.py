class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ans = [0 for i in range(len(nums))]
        nums = [(i, num) for i, num in enumerate(nums)]   
    
        def count_smaller(left, right, ans):
            left_ptr, right_ptr = 0, 0
            temp, cond = 0, False
            new = 0
            
            while left_ptr < len(left) and right_ptr < len(right):
                if cond:
                    temp += new
                if left[left_ptr][1] > right[right_ptr][1]:
                    new += 1
                    right_ptr += 1
                    cond = False
                else:
                    ans[left[left_ptr][0]] += new
                    left_ptr += 1
                    cond = True
            
            for i in range(left_ptr, len(left)):
                ans[left[i][0]] += new
        
        
        def merge(left, right):
            left_ptr, right_ptr = 0, 0
            new_arr = []
            while left_ptr < len(left) and right_ptr < len(right):
                
                if left[left_ptr][1] < right[right_ptr][1]:
                    new_arr.append(left[left_ptr])
                    left_ptr += 1
                else:
                    new_arr.append(right[right_ptr])
                    right_ptr +=1 
            new_arr.extend(left[left_ptr:])
            new_arr.extend(right[right_ptr:])
            
            return new_arr
        
        def merge_sort(nums, ans):
            
            if len(nums) <= 1:
                return nums
            
            mid = len(nums) // 2
            
            left = merge_sort(nums[:mid], ans)
            right = merge_sort(nums[mid:], ans)
            
            count_smaller(left, right, ans) 
            
            return merge(left, right)
        merge_sort(nums, ans)
        return ans