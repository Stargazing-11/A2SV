class Solution:
    def countVowels(self, word: str) -> int:
        res = 0
        vowels = ["a","e","i","o","u"]
        for i, j in enumerate(word):
            if j in vowels:
                res += i*(len(word)-i-1) + len(word)
        return res