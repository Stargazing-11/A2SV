class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seens = set()
        longest = 0
        left = 0
        
        for right in range(len(s)):
            while right < len(s) and s[right] in seens:
                longest = max(longest, len(seens))
                seens.remove(s[left])
                left += 1
            seens.add(s[right])
        
        return max(longest, len(seens))
