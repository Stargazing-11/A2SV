class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        
        found = False
        
        for ind, num in enumerate(nums):
            if num == target and found == False:
                ans[0] = ind
                ans[-1] = ind
                found = True
            elif num == target and found == True:
                ans[-1] = ind
        return ans