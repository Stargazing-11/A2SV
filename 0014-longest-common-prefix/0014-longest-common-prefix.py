class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = min(strs, key=len)        
        for word in strs:
            for index, char in enumerate(word):
                if index >= len(longest):
                    longest = longest[:index]                    
                elif char != longest[index]:
                    longest = longest[:index]
        return longest