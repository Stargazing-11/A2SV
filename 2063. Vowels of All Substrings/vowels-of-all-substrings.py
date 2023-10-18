class Solution:
    def countVowels(self, word: str) -> int:
        vowels = ["a", 'e', 'i', 'o', 'u']
        ans = 0
        
        for i, c in enumerate(word):
            if c in vowels:
                ans += ((i+1) * (len(word) - i))
        return ans