class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        cond = False
        for j, i in enumerate(s):
            if i == "]":
                cond = True
                out = []
                while(stk and stk[-1] != "["):
                    out.append(stk.pop())
                out.reverse()
                stk.pop()
                num = []
                while(stk and stk[-1].isdigit()):
                    num.append(stk.pop())
                num.reverse()
                y = "".join(num)
                z = "".join(out)
                stk.append(z * int(y))
                return self.decodeString("".join(stk) + s[j+1:])
            else:
                stk.append(i)
        if cond == False:
            return s