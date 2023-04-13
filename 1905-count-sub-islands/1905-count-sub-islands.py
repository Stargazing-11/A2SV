class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        visited = set()
        count = 0
        
        def inBound(row, col):
            return 0 <= row < len(grid2) and 0 <= col < len(grid2[0])
        
        def dfs(row, col, flg):
            visited.add((row, col))
            if not grid1[row][col]:
                flg[0] = False
                
            for r, c in directions:
                new_r = row + r
                new_c = col + c
                
                if inBound(new_r, new_c) and (new_r, new_c) not in visited and grid2[new_r][new_c]:
                    dfs(new_r, new_c, flg)
                    
                    
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if (i, j) not in visited and grid2[i][j]:
                    flg = [True]
                    dfs(i, j, flg)
                    if flg[0]:
                        count += 1
        return count
        