class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums = nums
        subSet = set()
        def backtrack(cur, nxt):
            if nxt >= len(nums):
                return 
            
            for i in range(nxt, len(nums)):
                if cur and cur[-1] <= nums[i]:
                    cur.append(nums[i])
                    if len(cur) > 1 and tuple(cur) not in subSet:
                        subSet.add(tuple(cur))
                        output.append(cur.copy())
                    backtrack(cur, i+1)
                    cur.pop()
            
        for i in range(len(nums)):
            backtrack([nums[i]], i+1)
        return output
    
   