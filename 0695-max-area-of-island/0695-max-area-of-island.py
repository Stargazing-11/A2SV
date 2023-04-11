class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = set()
        max_area = 0

        def inBound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        def dfs(row, col):
            nonlocal max_area, area
            visited.add((row, col))
            area += 1
            for r, c in directions:
                max_area = max(max_area, area)
                new_r = r + row
                new_c = c + col
                if inBound(new_r, new_c) and (new_r, new_c) not in visited and grid[new_r][new_c]:
                    dfs(new_r, new_c)
                    
        area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j]:
                    area = 0
                    dfs(i, j)
        return max_area