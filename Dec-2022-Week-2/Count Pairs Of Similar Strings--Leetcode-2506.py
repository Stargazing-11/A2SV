class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count = 0

        for index, word in enumerate(words):
            temp = "".join(sorted(set(word)))
            for idx, wrd in enumerate(words[index + 1:]):
                temp2 = "".join(sorted(set(wrd)))
                if temp == temp2:
                    count += 1
        return count
