class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True
        if n%3 != 0:
            return False
        if n == 3:
            return True
        n = n/3
        print(n)
        return self.isPowerOfThree(n)