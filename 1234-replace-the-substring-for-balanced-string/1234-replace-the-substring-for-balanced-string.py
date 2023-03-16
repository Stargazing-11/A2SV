class Solution:
    def balancedString(self, s: str) -> int:
        counter = Counter(s)
        target = (len(s) / 4)
        left = 0
        ans = len(s)
        
        for right, key in enumerate(s):
            counter[key] -= 1
            
            while left < len(s) and all(target >= counter[char] for char in "QWER"):
                ans = min(ans, right - left + 1)
                counter[s[left]] += 1
                left += 1
        return ans 