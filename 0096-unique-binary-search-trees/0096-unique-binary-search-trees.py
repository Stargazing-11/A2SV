class Solution:
    def numTrees(self, n: int) -> int:
        
        cache = [1] * (n + 1)
        
        for i in range(2, n + 1):
            total = 0
            for j in range(1, i + 1):
                left = j - 1
                right = i - j 
                
                total += cache[left] * cache[right]
            cache[i] = total
        return cache[n]