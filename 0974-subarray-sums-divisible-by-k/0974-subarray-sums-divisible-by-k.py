class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        prefs = {0:1}
        
        count = 0
        prefSum = 0
        for num in nums:
            prefSum += num 
            if prefSum % k in prefs:
                count += prefs[prefSum % k]
                
            if prefSum % k in prefs:
                prefs[prefSum%k] += 1
            else:
                prefs[prefSum%k] = 1
        return count