class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        
        cache = {}
        
        paths = [(1,-2), (2,-1), (2,1), (1,2), (-1,2), (-2,1), (-2,-1), (-1,-2)]
        
        def isIn(r, c):
            return 0 <= r < n and 0 <= c < n

        c = k
        def dp(r, c, moves):
            if not isIn(r, c):
                return 0
            
            if moves == 0:
                return 1
            
            if (r, c,moves) in cache:
                return cache[(r,c,moves)]
            
            cache[(r,c,moves)] = 0
            
            for i, j in paths:
                cache[(r, c, moves)] += dp(r+i, c+j, moves-1)
            return cache[(r,c,moves)]

        return dp(row, column,k) / (8 ** c)