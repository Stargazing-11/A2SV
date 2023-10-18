class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0
        
        def getFrequent(freq_store, exclude):
            max_freq = (0, 0)
            for key in freq_store.keys():
                
                if key == exclude:
                    continue
                if max_freq[1] < freq_store[key]:
                    max_freq = (key, freq_store[key])
            if max_freq == (0, 0):
                return (None, None)
            return max_freq
        
        def getAns(max_even, max_odd):
            if max_odd == None and max_even == None:
                return len(nums)
            if max_odd == None:
                return odd_count
            if max_even == None:
                return even_count
            return len(nums) - (odds[max_odd] + evens[max_even])
        
        odds, evens = defaultdict(int), defaultdict(int)
        odd_count, even_count = 0, 0
        for i, num in enumerate(nums):
            if i % 2:
                odds[num] += 1
                odd_count += 1
            else:
                evens[num] += 1
                even_count += 1
        
        max_odd1 = getFrequent(odds, None)[0]
        max_even1 = getFrequent(evens, None)[0]
        
        max_odd2 = getFrequent(odds, max_odd1)[0]
        max_even2 = getFrequent(evens, max_even1)[0]
        
        even_max = [max_even1, max_even2]        
        odd_max = [max_odd1, max_odd2]
            
        ans = len(nums)
        for i in range(2):
            for j in range(2):
                if even_max[i] != odd_max[j]:
                    ans = min(ans, getAns(even_max[i], odd_max[j]))
        return ans 