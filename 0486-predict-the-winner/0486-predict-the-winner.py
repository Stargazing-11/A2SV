class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def predict(left, right):
            if left > right:
                return 0
            
            choice1 = nums[left] + min(predict(left+2, right), predict(left+1, right-1))
            choice2 = nums[right] + min(predict(left+1, right-1), predict(left, right-2))
            
            return max(choice1, choice2)
            
        return 2*(predict(0, len(nums)-1)) >= sum(nums)