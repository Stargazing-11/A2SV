class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        prefs = {0: 1}
        pref_sum = 0
        subArrays = 0
        
        for num in nums:
            pref_sum += num
            
            if pref_sum - goal in prefs:
                subArrays += prefs[pref_sum - goal]
            
            prefs[pref_sum] = prefs.get(pref_sum, 0) + 1
        return subArrays