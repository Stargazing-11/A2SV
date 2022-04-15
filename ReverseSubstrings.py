class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        stk = []
        output = []
        temp = []
        for i in s:
            if i !=")":
                stk.append(i)
            else:
                print(stk)
                for j in stk[::-1]:
                    print(j)
                    if j != "(":
                        k = stk.pop()
                        temp.append(k)
                        print(temp, "temp")
                    else:
                        stk.pop()
                        print(stk, "stk first")
                        break
                temp.reverse
                stk.extend(temp)
                temp.clear()
                print(stk, "stk")
        st = ""
        return st.join(stk)