class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stk = []
        
        for i in range(len(s)):
            
            if not stk or stk[-1][0] != s[i]:
                stk.append([s[i], 1])
                continue
            
            if stk[-1][0] == s[i]:
                stk[-1][1] += 1
                
            if stk[-1][1] == k:
                stk.pop()
        ans = []
        
        for s, i in stk:
            ans.append(s * i)
        
        return "".join(ans)