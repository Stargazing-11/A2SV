class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        c = Counter(nums)
        count = 0
        seen = set()
        for i in c:
            if i not in seen and (k-i) in c:
                if i == (k-i):
                    count +=c[i]//2
                else:
                    count += min(c[i], c[k-i])
                seen.add(i)
                seen.add(k-i)
        return count
        