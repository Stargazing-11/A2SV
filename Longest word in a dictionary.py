class Solution:
    def longestWord(self, words: List[str]) -> str:
        words = sorted(words, key=lambda x:[len(x), x])
        print(words)
        trie = {}
        longest = ""
        for word in words:
            cur = trie
            for i, letter in enumerate(word):
                if letter in cur:
                    cur = cur[letter]
                else: 
                    if i<len(word)-1:
                        break
                    else:
                        cur[letter] = {}
            else:
                longest = max(longest, word, key = lambda x:len(x))
        
        return longest
