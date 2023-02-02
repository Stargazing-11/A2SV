class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        word1 = words[0]
        for word in words[1:]:
            for i in range(max(len(word), len(word1))):
                if i >= len(word):
                    return False
                elif i >= len(word1):
                    break
                if order.index(word1[i]) < order.index(word[i]):
                    word1 = word
                    break
                elif order.index(word1[i]) <= order.index(word[i]):
                    continue
                else:
                    return False
        return True