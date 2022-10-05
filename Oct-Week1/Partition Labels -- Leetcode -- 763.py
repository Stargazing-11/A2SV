from collections import Counter

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counted = Counter(s)
        
        temp = {s[0]:counted[s[0]]}
        ans = []
        count = 0
        
        for i in s:
            # print(i,counted[i], temp, "top", ans)
            if len(temp) == 0:
                ans.append(count)
                count = 0
            if i in temp:
                temp[i] -= 1
            if i not in temp and counted[i] > 1:
                    temp[i] = counted[i] - 1
            count += 1
            # print(temp, i, counted[i], "mid")
            if i in temp and temp[i] == 0:
                del temp[i]
            # print(ans)
        if count > 0:
            ans.append(count)
        return ans