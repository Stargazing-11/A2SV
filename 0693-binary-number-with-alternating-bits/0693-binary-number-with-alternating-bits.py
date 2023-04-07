class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        print(4 ^ 1)
        
        check = n & 1
        n = (n >> 1)
        while n > 0:
            if n & 1 == check:
                return False
            check = n & 1
            n = (n >> 1)
        return True