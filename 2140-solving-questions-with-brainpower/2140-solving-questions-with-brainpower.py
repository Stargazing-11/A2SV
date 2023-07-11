class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = {}
        
        def dp_func(index):
            
            if index >= len(questions):
                return 0
            
            if index in dp:
                return dp[index]
            
            pt, brp = questions[index]
            
            dp[index] = max(pt + dp_func(index + brp + 1), dp_func(index + 1))
            
            return dp[index]
        
        return dp_func(0)