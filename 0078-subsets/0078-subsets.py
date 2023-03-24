class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        output = [[]]
        subSet = set()
        def backtrack(start, cur):
            if start >= len(nums):
                return 
            
            for i in range(start, len(nums)):
                cur.append(nums[start])
                if len(set(cur)) == len(cur):
                    if tuple(cur) not in subSet:
                        output.append(cur.copy())
                        subSet.add(tuple(cur))
                    backtrack(i+1, cur)
                cur.pop()
                
        for i in range(len(nums)):
            backtrack(i, [])
        return output