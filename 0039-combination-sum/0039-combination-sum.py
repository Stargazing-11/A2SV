class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        def backtrack(cur, candidates, curSum, target, curelem):
            if curSum >= target:
                if curSum == target:
                    output.append(cur.copy())
                return 

            for i in range(curelem, len(candidates)):
                cur.append(candidates[i])
                curSum += candidates[i]
                backtrack(cur, candidates, curSum, target, i)
                curSum -= cur.pop()
                
        for i in range(len(candidates)):
            backtrack([candidates[i]], candidates, candidates[i], target, i)
        return output