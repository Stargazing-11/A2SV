class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        cache = {}
        
        def checkRow(row):
            if not (0 <= row < len(matrix)):
                return False
            return True
        
        def checkCol(col):
            if not(0 <= col < len(matrix[0])):
                return False
            return True
        
        
        def dp(row, col):
            
            if not checkRow(row):
                return 0
            
            if not checkCol(col):
                return float('inf')
            
            if (row, col) in cache:
                return cache[(row, col)]
            cache[(row, col)] = min(dp(row+1, col-1), dp(row+1, col), dp(row+1, col+1)) + matrix[row][col]
            
            return cache[(row, col)]
        
        ans = float('inf')
        for i in range(len(matrix[0])):
            ans = min(ans, dp(0, i))
        
        return ans