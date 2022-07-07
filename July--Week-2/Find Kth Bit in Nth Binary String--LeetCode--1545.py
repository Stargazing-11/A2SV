class Solution:
    def inv(self, s):
        ret = ""
        for i in s:
            if i == "0":
                ret += "1"
            else:
                ret += "0"
        ret= ret[::-1]
        return ret
    
    def findKthBit(self, n: int, k: int) -> str:
        s = ['0']
        for i in range(1, n):
            temp = s[i - 1] + '1' + self.inv(s[i-1])
            s.append(temp)
        return s[-1][k-1]