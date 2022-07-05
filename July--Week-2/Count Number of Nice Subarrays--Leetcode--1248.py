class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefixsum = collections.defaultdict(int)
        total, ans, prefixsum[0] =0, 0, 1
        for i in range(len(nums)):
            total += nums[i] & 1
            ans += prefixsum[total-k]
            prefixsum[total] += 1
        return ans