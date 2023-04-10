class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def inBound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        directions = [(-1, 0), (0, -1), (0,1), (1, 0)]
        visited = set()
        count = 0
        
        def dfs(row, col):
            
            visited.add((row, col))
            
            for i, j in directions:
                newRow = row + i
                newCol = col + j
                if inBound(newRow, newCol) and (newRow, newCol) not in visited and grid[newRow][newCol] == "1":
                    dfs(newRow, newCol)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if inBound(i, j) and (i, j) not in visited and grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        return count