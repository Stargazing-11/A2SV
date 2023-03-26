class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        output = []
        def backtrack(cur, nxt):
            if len(cur) == 4 and nxt < len(s):
                return
            elif len(cur) == 4 and nxt >= len(s):
                output.append(".".join(cur))
                return 
            
            for i in range(nxt, len(s)):
                if int(s[nxt:i+1]) <= 255:
                    if len(s[nxt:i+1]) > 1 and s[nxt] == "0":
                        return 
                    cur.append(s[nxt:i+1])
                    backtrack(cur, i+1)
                    cur.pop()
                elif int(s[:i+1]) > 255:
                    return
            return 
    
        for i in range(len(s)):
            if int(s[:i+1]) <= 255: 
                if len(s[:i+1]) > 1 and s[0] == "0":
                    break
                backtrack([s[:i+1]], i+1)
        return output