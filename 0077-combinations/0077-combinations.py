class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        output = []
        def backtrack(cur, n, k):
            if len(cur) == k:
                output.append(cur.copy())
                return 

            for i in range(cur[-1] + 1, n + 1):
                cur.append(i)
                backtrack(cur, n, k)
                cur.pop()
        
        for i in range(1, n + 1):
            backtrack([i], n, k)
        return output