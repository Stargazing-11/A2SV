class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        new = x ^ y 
        print(new)
        c = 0
        while (new > 0):
            new = new & new -1
            c += 1
        return c