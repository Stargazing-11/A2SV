class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stk = ["/"]
        temp = []
        
        for char in path:
            if char != "/":
                temp.append(char)
            else:
                temp = "".join(temp)
                if temp == ".." and len(stk) > 1:
                    stk.pop()
                    stk.pop()
                elif temp != "." and temp != "" and temp != "..":
                    stk.append(temp)
                    stk.append("/")
                temp = []
        temp = "".join(temp)
        if temp == ".." and len(stk) > 1:
            stk.pop()
            stk.pop()
        elif temp != ".." and temp != "." and temp != "":
            stk.append(temp)
        if stk[-1] == "/" and len(stk) > 1:
            stk.pop()
        return "".join(stk)
                    