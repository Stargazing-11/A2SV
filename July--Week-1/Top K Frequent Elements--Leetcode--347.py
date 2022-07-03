from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        z = Counter(nums)
        y = sorted(z, key=z.get, reverse=True)
        c = 0
        out = []
        while(c < k):
            out.append(y[c])
            c += 1
        return out