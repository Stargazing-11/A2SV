class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        operands = {"*", "/", "+", "-"}
        
        for tkn in tokens:
            if tkn not in operands:
                stk.append(tkn)
            else:
                a = int(stk.pop())
                b = int(stk.pop())
                if tkn == "+":
                    stk.append(b + a)
                elif tkn == "-":
                    stk.append(b - a)
                elif tkn == "*":
                    stk.append(b * a)
                else:
                    stk.append(b / a)
        return int(stk[0])