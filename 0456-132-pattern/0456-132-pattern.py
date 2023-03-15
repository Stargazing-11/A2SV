class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        monStk = []
        minVal = nums[0]
        
        for num in nums[1:]:
            while monStk and monStk[-1][0] <= num:
                monStk.pop()
            
            if monStk and monStk[-1][1] < num:
                return True
            monStk.append((num, minVal))
            minVal = min(minVal, num)
        return False