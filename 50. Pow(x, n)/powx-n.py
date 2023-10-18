class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = -n
            x = 1 /x
            
        def helper(x, n):
            if n == 0:
                return 1
            result = helper(x, n//2)
            result *= result
            return x * result  if n % 2 else result 
        return helper(x,n)