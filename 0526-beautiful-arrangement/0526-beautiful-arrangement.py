class Solution:
    def countArrangement(self, n: int) -> int:                      
        count = [0]
        visited = set()
        def backtrack(pos):
            if pos > n:
                count[0] += 1
                return     
            for i in range(1, n+1):
                if i in visited or not ((i%pos) == 0 or (pos % i) == 0):
                    continue
                visited.add(i)
                backtrack(pos+1)
                visited.remove(i)
            
            return
        
        for i in range(1, n+1):
            visited.clear()
            visited.add(i)
            backtrack(2)
        return count[0]
                
                
                
                
                
                
                
                
                
                
                
                
                
                