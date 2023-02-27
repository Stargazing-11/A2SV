class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefMul1 = [1]
        prefMul2 = [1]
        ans = []
        for i in range(1, len(nums) + 1):
            prefMul1.append(prefMul1[-1] * nums[i-1])
            prefMul2.append(prefMul2[-1] * nums[-i])
        prefMul2.reverse()
        for i in range(1, len(prefMul1)):
            ans.append(prefMul1[i-1] * prefMul2[i])
        return ans