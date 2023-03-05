class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invertThenReverse(string):
            string = ["1" if i == "0" else "0" for i in string]
            string.reverse()
            return "".join(string)
        
        def operate(n):
            if n == 1:
                return "0"
            string = operate(n-1)
            return string + "1" + invertThenReverse(string)
        output = operate(n)
        return output[k-1]