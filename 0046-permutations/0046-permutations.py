class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        def backtrack(curSet, cur):
            if len(cur) == len(nums):
                output.append(cur.copy())
                return 
            
            for i in range(len(nums)):
                if curSet & (1<<i):
                    continue
                curSet = curSet | (1<<i)
                cur.append(nums[i])
                backtrack(curSet, cur)
                curSet = curSet & ~(1<<i)
                cur.pop()
                
        curSet = 0
        for i in range(len(nums)):
            curSet = 0
            curSet = curSet | (1<<i)
            backtrack(curSet, [nums[i]])
        return output