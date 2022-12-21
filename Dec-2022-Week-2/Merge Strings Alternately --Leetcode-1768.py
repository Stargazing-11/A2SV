class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = []
        for i in range(min(len(word1), len(word2))):
            output.append(word1[i])
            output.append(word2[i])

        if len(word1) > len(word2):
            output.append(word1[len(word2):])
        elif len(word2) > len(word1):
            output.append(word2[len(word1):])
        return "".join(output)
