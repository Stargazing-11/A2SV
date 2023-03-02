class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = [-1 for _ in range(len(nums))]
        
        mon_stk = []
        for _ in range(2):
            for i in range(len(nums)):
                while mon_stk and nums[mon_stk[-1]] < nums[i]:
                    ans[mon_stk.pop()] = nums[i]
                mon_stk.append(i)
        return ans