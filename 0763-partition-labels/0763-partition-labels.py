class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []
        counted = Counter(s)
        seens = set()
        last = 0
        for i in range(len(s)):
            if i == 0:
                seens.add(s[i])
            elif i > 0 and len(seens) == 0:
                ans.append(i - last)
                last = i
            
            counted[s[i]] -= 1
                
            if counted[s[i]] > 0:
                seens.add(s[i])
            elif counted[s[i]] == 0 and s[i] in seens:
                seens.remove(s[i])
                
        ans.append(i + 1 - last)
        return ans