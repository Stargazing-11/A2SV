class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def predict(l, r):
            if l > r:
                return 0
            
            choice1 = nums[l] + min(predict(l+2, r), predict(l+1, r-1))
            
            choice2 = nums[r] + min(predict(l+1, r-1), predict(l, r-2))
            
            return max(choice1, choice2)
            
        return 2*(predict(0, len(nums)-1)) >= sum(nums)