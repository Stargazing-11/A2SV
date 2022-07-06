class Solution(object):
    def PredictTheWinner(self, nums):
        n = len(nums)
        def dfs(i, j):
            if i == j:
                return nums[i]

            left = nums[i] - dfs(i+1, j)
            right = nums[j] - dfs(i, j-1)
            
            return max(left, right)
        
        return dfs(0, n-1) >= 0