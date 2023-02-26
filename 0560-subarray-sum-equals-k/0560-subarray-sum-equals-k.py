class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        dicts = {0:1}
        
        prefSum = 0
        for num in nums:
            prefSum += num
            
            if prefSum - k  in dicts:
                count += dicts[prefSum - k]
            if prefSum in dicts:
                dicts[prefSum] += 1
            else:
                dicts[prefSum] = 1
        return count 