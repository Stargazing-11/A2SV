class Solution:
    def splitString(self, s: str) -> bool:
            
        if len(s) == 1:
            return False
        
        def backtrack(cur, s):
            if len(s) == 1 and cur - int(s) == 1 or len(s) == 0:
                    return True
            elif len(s) <= 1:
                return False

            newcur = 0
            ans = False
            for i in range(len(s)):
                newcur = (newcur*10) + int(s[i])
                if int(cur) - int(newcur) == 1:
                    ans = backtrack(newcur, s[i+1:]) 
                elif int(newcur) - int(cur) > 1:
                    return False
                if ans:
                    break
            return ans
        
        first = 0
        for i in range(len(s) - 1):
            first = (first*10) + int(s[i])
            ans = backtrack(first, s[i+1:])
            if ans:
                break
        return ans 