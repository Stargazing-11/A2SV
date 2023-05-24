class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:

        parents = {(i,j):(i,j) for i in range(len(grid)) for j in range(len(grid[0]))}        
        rank = {(i,j): 1 for i in range(len(grid)) for j in range(len(grid[0]))}
        
        def find(node):
            root = node
            while root != parents[root]:
                root = parents[root]
            
            while node != parents[node]:
                temp = parents[node]
                parents[node] = root
                node = temp
            return root
        
        def union(node1, node2):
            p1, p2 = find(node1), find(node2)
            
            if rank[node1] < rank[node2]:
                p1, p2 = p2, p1
            
            parents[p2] = p1
            rank[p1] += rank[p2]
        
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
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                (row1, col1), (row2, col2) = directions[grid[i][j]]

                if inBound(i + row1, j + col1) and (-row1, -col1) in directions[grid[i+row1][j+col1]]:
                    union((i,j), (i+row1, j+col1))

                if inBound(i + row2, j + col2) and (-row2, -col2) in directions[grid[i+row2][j+col2]]:
                    union((i,j), (i+row2, j+col2))

        
        return find((0,0)) == find((len(grid)-1, len(grid[0])-1))
        
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    