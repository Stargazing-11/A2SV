class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        leng = 0
        stk = []
        for i in s:
            if i not in stk:
                stk.append(i)
            else:
                leng = max(leng, len(stk))
                while(stk[0] != i):
                    stk.pop(0)
                stk.pop(0)
                stk.append(i)
        return max(leng, len(stk))