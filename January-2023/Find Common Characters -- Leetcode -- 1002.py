class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans = []
        counted = Counter(words[0])
        counted = {x: [counted[x], 1] for x in counted.keys()}

        for word in words[1:]:
            temp = Counter(word)
            for key in temp.keys():
                if key in counted:
                    if temp[key] < counted[key][0]:
                        counted[key] = [temp[key], counted[key][1] + 1]
                    else:
                        counted[key][1] += 1

        for key in counted.keys():
            if counted[key][1] == len(words):
                ans += [key for i in range(counted[key][0])]
        return ans
