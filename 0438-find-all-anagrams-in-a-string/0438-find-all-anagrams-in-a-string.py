class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        pCounted = Counter(p)
        wind = Counter(s[:k])
        
        ans = []
        
        if wind == pCounted:
            ans.append(0)
        left, right = 1, k
        
        while right < len(s):
            wind[s[left-1]] -= 1
            wind[s[right]] += 1
            
            if wind[s[left-1]] == 0:
                del wind[s[left-1]]
            if wind == pCounted:
                ans.append(left)
            left += 1
            right += 1
        return ans