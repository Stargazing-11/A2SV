class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        def findTriFib(n):
            if n == 1 or n == 2:
                return 1
            if n == 0:
                return 0

            if n not in memo:
                memo[n] = findTriFib(n-1) + findTriFib(n-2) + findTriFib(n-3)
            return memo[n]
        
        return findTriFib(n)