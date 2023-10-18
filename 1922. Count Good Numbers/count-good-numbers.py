class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        ans = pow(20, n // 2, (10 ** 9 + 7))
        ans *= 5 if n % 2 else 1
        
        return ans % (10 **9 + 7)