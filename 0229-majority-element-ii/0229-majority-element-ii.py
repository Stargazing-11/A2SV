from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        z = Counter(nums)
        n = len(nums)//3
        out = []
        z = z.most_common()
        for i in z:
            if i[1] > n:
                out.append(i[0])
        return out