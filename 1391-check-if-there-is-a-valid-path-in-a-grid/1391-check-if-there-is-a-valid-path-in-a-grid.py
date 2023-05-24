class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        
        directions = defaultdict(set)
        
        for i in range(1, 7):
            if i == 1:
                directions[i] = {(0, -1), (0, 1)}      
            if i == 2:
                directions[i] = {(1, 0), (-1, 0)}
            if i == 3:
                directions[i] = {(1, 0),(0, -1)}
            if i == 4:
                directions[i] = {(0, 1), (1, 0)}
            if i == 5:
                directions[i] = {(-1, 0),(0, -1)}
            if i == 6:
                directions[i] = {(-1, 0), (0, 1)}
        
        def inBound(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])
        
        visited = set()
        def dfs(node):
            visited.add(node)
            row, col = node

            for r, c in directions[grid[row][col]]:
                new_row, new_col = r + row, c + col
                
                if inBound(new_row, new_col) and (new_row, new_col) not in visited: 

                    if (r * -1, c * -1) in directions[grid[new_row][new_col]]:
                        dfs((new_row, new_col))
            
        dfs((0, 0))
        
        if (len(grid)-1, len(grid[0])-1) in visited:
            return True
        return False
        
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    