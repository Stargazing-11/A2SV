class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        
        maxOr = 0
        for num in nums:
            maxOr = maxOr | num
        
        output = 0
        
        def backtrack(start, cur):
            nonlocal output 
            if start >= len(nums):
                return 
            
            for i in range(start, len(nums)):
                new = cur[-1] | nums[i]
                if new == maxOr:
                    output += 1
                cur.append(new)
                backtrack(i+1, cur)
                cur.pop()
            return 
        for i in range(len(nums)):
            if nums[i] == maxOr:
                output += 1
            backtrack(i+1, [nums[i]])
        return output