class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pref_sum = [0]
        
        for num in nums:
            pref_sum.append(pref_sum[-1] + num)
        
        for i in range(1, len(pref_sum)):
            cur = pref_sum[-1] - pref_sum[i]
            if pref_sum[i-1] == cur:
                return i - 1
        return -1