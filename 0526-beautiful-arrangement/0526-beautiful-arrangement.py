class Solution:
    def countArrangement(self, n: int) -> int:                      
        count = [0]
        visited = 0
        def backtrack(pos):
            nonlocal visited
            if pos > n:
                count[0] += 1
                return     
            for i in range(1, n+1):
                if visited & (1<<(i-1)) or not ((i%pos) == 0 or (pos % i) == 0):
                    continue
                visited = visited | (1 << (i-1))
                backtrack(pos+1)
                visited = visited & ~(1<<(i-1))            
            return
        
        for i in range(1, n+1):
            visited = (1<<(i-1))
            backtrack(2)
        return count[0]
                
                
                
                
                
                
                
                
                
                
                
                
                
                