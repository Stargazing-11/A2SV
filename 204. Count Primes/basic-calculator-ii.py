class Solution:
    def calculate(self, s: str) -> int:
        stk = []
        ans = 0
        while(s):
            i = s[0]
            s = s[1:]
            while(i.isdigit() and s and s[0].isdigit()):
                i += s[0]
                s = s[1:]
            if i == "*":
                x = int(stk.pop())
                y = []
                while(s[0] == " "):
                    s = s[1:]
                
                while(s and s[0].isdigit()):
                    y.append(s[0])
                    s = s[1:]
                if y:
                    y = "".join(y)
                    y = int(y)
                else:
                    y = 1
                z = x * y
                stk.append(str(z))
            elif i == "/":
                x = int(stk.pop())
                y = []
                while(s[0] == " "):
                    s = s[1:]
                while(s and s[0].isdigit()):
                    y.append(s[0])
                    s = s[1:]
                if y:
                    y = "".join(y)
                    y = int(y)
                else:
                    y = 1
                z = x // y
                stk.append(str(z))
            elif i == " ":
                continue
            else:
                stk.append(i)
        if len(stk) == 1:
            return int(stk[0])
        while(stk):
            stk = "".join(stk)
            ans = eval(stk)
            break
        return ans