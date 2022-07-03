class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        stk = []
        for i in matrix:
            stk += i
        stk.sort()
        return stk[k-1]
        