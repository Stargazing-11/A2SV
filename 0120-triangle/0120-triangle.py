class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        dp = {}
        
        def func(row_idx, index):
            
            if row_idx >= len(triangle):
                return 0
            
            if (row_idx, index) in dp:
                return dp[(row_idx, index)]
            
            min_sum = float('inf')
            
            for i in range(index, min(index + 2, len(triangle[row_idx]))):
                min_sum = min(min_sum, func(row_idx + 1, i) + triangle[row_idx][i])
            
            dp[(row_idx, index)] = min_sum
            return dp[(row_idx, index)]
        
        return func(0, 0)