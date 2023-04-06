class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        def backtrack(curSet, cur):
            if len(cur) == len(nums):
                output.append(cur.copy())
                return 
            
            for i in range(len(nums)):
                if nums[i] in curSet:
                    continue
                curSet.add(nums[i])
                cur.append(nums[i])
                backtrack(curSet, cur)
                curSet.remove(nums[i])
                cur.pop()
                
        curSet = set()
        for i in range(len(nums)):
            curSet.clear()
            curSet.add(nums[i])
            backtrack(curSet, [nums[i]])
        return output