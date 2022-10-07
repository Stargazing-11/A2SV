from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pCounted, sCounted = Counter(p), Counter(s[:len(p)])

        left, right = 0, len(p) - 1

        indexs = []
        condition = False

        while right < len(s):
            for i in pCounted:
                if pCounted[i] != sCounted[i]:
                    condition = True
                    break
            if condition == False:
                indexs.append(left)

            condition = False
            sCounted[s[left]] -= 1

            if sCounted[s[left]] == 0:
                del sCounted[s[left]]
            left += 1
            right += 1

            if right >= len(s):
                break
            if s[right] in sCounted:
                sCounted[s[right]] += 1
            else:
                sCounted[s[right]] = 1
        return indexs
