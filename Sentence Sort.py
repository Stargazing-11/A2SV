class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        x = [0 for i in range(len(s))]
        k = " "
        for j in s:
            # print(j[-1])
            y = int(j[-1])
            x[y-1] = j[:-1]
        x =k.join(x)
        return x
    
