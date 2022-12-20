class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()

        for i, j in enumerate(t):
            if len(s) == i or s[i] != j:
                return j
