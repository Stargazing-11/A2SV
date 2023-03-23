class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)
        if len(s) == 1:
            return False
        
        def backtrack(cur, nxt, candidate):
            
            if n - nxt <= 1:
                if n - nxt == 0:
                    return True
                elif cur - int(candidate[nxt]) == 1:
                    return True
                else:
                    return False
                
            newcur = 0
            ans = False
            for i in range(nxt, len(candidate)):
                newcur = (newcur*10) + int(candidate[i])
                
                if int(cur) - int(newcur) == 1:
                    ans = backtrack(newcur, i+1, candidate) 
                elif int(newcur) - int(cur) > 1:
                    return False
                if ans:
                    break
            return ans
        
        first = 0
        for i in range(len(s) - 1):
            first = (first*10) + int(s[i])
            ans = backtrack(first, i+1, s)
            if ans:
                break
        return ans 