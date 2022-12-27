class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        
        k = 1
        while(True):
            print(k)
            if (n * k) % 2 == 0:
                return n * k
            else:
                k += 1