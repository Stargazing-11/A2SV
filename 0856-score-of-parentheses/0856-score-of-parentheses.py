class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stk = []
        
        for par in s:
            if par == ")":
                ans = 0
                while stk[-1] != "(":
                    ans += stk.pop()
                stk.pop()
                if ans == 0:
                    stk.append(1)
                else:
                    stk.append(ans * 2)
                continue
            stk.append(par)
        return sum(stk)
        
        
        
        
        
#     "(()(()))"