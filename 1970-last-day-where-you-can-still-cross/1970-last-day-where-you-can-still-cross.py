class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        
        union_find = UnionFind(row, col)
        
        def inBound(r, c):
            return 0 <= r < row and 0 <= c < col
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)] 

        grid = [[1 for i in range(col)] for j in range(row)]

        for i in range(len(cells) -1, -1, -1):
            r, c = cells[i]
            grid[r-1][c-1] = 0
            node1 = (r-1, c-1)
            for dr, dc in directions:
                new_r, new_c = r + dr - 1, dc + c - 1
                node2 = (new_r, new_c)
                
                if inBound(new_r, new_c) and grid[new_r][new_c] == 0:
                    union_find.union(node1, node2)
            
            
            if r == 1:
                union_find.union((-1,-1), node1)
            
            if r == row:
                union_find.union((row, col), node1)
            
            if union_find.find((-1,-1)) == union_find.find((row, col)):
                return i
            
        
class UnionFind:
    def __init__(self, row, col):
        self.parents = {}
        self.rank = {}
        
        self.parents[(-1, -1)] = (-1, -1)
        self.parents[(row, col)] = (row, col)
        
        self.rank[(-1, -1)] = 1
        self.rank[(row, col)] = 1
        
        for i in range(row):
            for j in range(col):
                self.parents[(i, j)] = (i, j)
                self.rank[(i, j)] = 1
                
    
    def find(self, node):
        root = node
        while root != self.parents[root]:
            root = self.parents[root]

        while node != self.parents[node]:
            temp = self.parents[node]
            self.parents[node] = root
            node = temp
        return root
        
    def union(self, a, b):

        p1, p2 = self.find(a), self.find(b)

        if self.rank[a] > self.rank[b]:
            p1, p2 = p2, p1
        
        self.parents[p1] = p2
        self.rank[p2] += self.rank[p1]
