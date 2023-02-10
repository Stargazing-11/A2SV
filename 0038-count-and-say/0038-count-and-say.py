from collections import Counter
class Solution:
    def countAndSay(self, n: int) -> str:
        ans = "1"
        for i in range(n-1):
            if len(ans) == 1:
                ans = "1" + ans[0]
                continue
            newans = ""
            count = 0
            temp = ans[0]
            for j in ans:
                if j != temp:
                    newans += str(count) + temp
                    temp = j
                    count = 0
                count += 1
            if count > 0:
                newans += str(count) + temp
            ans = newans
        return ans
    