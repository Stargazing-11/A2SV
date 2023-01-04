class Solution:
    def printVertically(self, s: str) -> List[str]:
        hashMap = defaultdict(list)
        words = s.split()
        maxLen = max(map(len, words))

        for word in words:
            for i in range(maxLen):
                if i < len(word):
                    hashMap[i].append(word[i])
                else:
                    hashMap[i].append(" ")

        ans = []
        for key in hashMap:
            while hashMap[key][-1] == " ":
                hashMap[key].pop()
            ans.append("".join(hashMap[key]))
        return ans
