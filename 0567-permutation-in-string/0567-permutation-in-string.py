class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        seenS1 = defaultdict(int)
        seenS2 = defaultdict(int)
        for i in range(len(s1)):
            seenS1[s1[i]] += 1
            seenS2[s2[i]] += 1
        
        if seenS1 == seenS2:
                return True
        left, right = 1, len(s1)
        while right < len(s2):
            seenS2[s2[left-1]] -= 1
            if seenS2[s2[left-1]] == 0:
                del seenS2[s2[left-1]]
            seenS2[s2[right]] += 1
            if seenS1 == seenS2:
                return True
            left += 1
            right += 1
        return False