class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        top, down = 0, 0
        ans = []

        while top < len(word1) and down < len(word2):
            if word1[top] == word2[down]:
                if word1[top:] >= word2[down:]:
                    ans.append(word1[top])
                    top += 1
                else:
                    ans.append(word2[down])
                    down += 1
            elif word1[top] > word2[down]:
                ans.append(word1[top])
                top += 1
            else:
                ans.append(word2[down])
                down += 1

        ans = "".join(ans) + word1[top:] + word2[down:]
        return ans
