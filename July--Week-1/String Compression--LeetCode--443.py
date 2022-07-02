from collections import Counter
class Solution:
    def compress(self, chars: List[str]) -> int:
        stk = []
        newchars = []
        for j, i in enumerate(chars):
            if not stk:
                stk.append(i)
                continue
            elif i == stk[-1]:
                stk.append(i)
                continue
            else:
                count = 0
                z = stk[-1]
                while(stk):
                    stk.pop()
                    count += 1
                newchars.append(z)
                if count > 1:
                    if count >= 10:
                        s = str(count)
                        # print(s)
                        for m in s:
                            newchars.append(m)
                    else:
                        newchars.append(str(count))
            stk.append(i)
        count = 0
        z = stk[-1]
        while(stk):
            stk.pop()
            count+=1
        newchars.append(z)
        if count > 1:
            if count >= 10:
                s = str(count)
                for i in s:
                    newchars.append(i)
            else:
                newchars.append(str(count))
        for i, j in enumerate(newchars):
            chars[i] = j
        while(len(chars) != len(newchars)):
            chars.pop()