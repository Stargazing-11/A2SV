class Solution:
    def removeKdigits(self, num: str, k: int) -> str:  
        stk = []
        if k == len(num):
            return "0"
        for i, j in enumerate(num):
            while (stk and k>0 and int(stk[-1]) > int(j)):
                stk.pop()
                k-=1
            stk.append(j)
        while(k>0):
            stk.pop()
            k-=1
        stk = "".join(stk)    
        return str(int(stk))