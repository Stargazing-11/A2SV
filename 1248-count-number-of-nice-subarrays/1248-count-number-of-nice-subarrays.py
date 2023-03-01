class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefs = {0:1}
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
        
#         counts = [0]
        
#         for i in range(1, len(nums) + 1):
#             if nums[i-1] == 0:
#                 counts.append(counts[i - 1])
#             else:
#                 counts.append(counts[i-1] + 1)
#         print(counts)
        
        pref_sum = 0
        ans = 0
        for num in nums:
            pref_sum += num
            
            if pref_sum - k in prefs:
                ans += prefs[pref_sum-k]
            if pref_sum in prefs:
                prefs[pref_sum] += 1
            else:
                prefs[pref_sum] = 1
        return ans