class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        def predict(l, r, memo):
            state = (l, r)
            if state in memo:
                return memo[state]
            if l > r:
                return 0
            
            choice1 = nums[l] + min(predict(l+2, r, memo), predict(l+1, r-1, memo))
            
            choice2 = nums[r] + min(predict(l+1, r-1, memo), predict(l, r-2, memo))
            
            memo[state] = max(choice1, choice2)
            return max(choice1, choice2)
            
        return 2*(predict(0, len(nums)-1, {})) >= sum(nums)