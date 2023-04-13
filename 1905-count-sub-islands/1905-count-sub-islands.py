class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        
        def inBound(row, col):
            return 0 <= row < len(grid2) and 0 <= col < len(grid2[0])
        
        paths = []
        visited = set()
        def dfs(row, col, cur):
            visited.add((row, col))
            cur.append((row, col))
            for r, c in directions:
                new_r = row + r
                new_c = col + c
                
                if inBound(new_r, new_c) and (new_r, new_c) not in visited and grid2[new_r][new_c]:
                    dfs(new_r, new_c, cur)
        
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if (i, j) not in visited and grid2[i][j]:
                    cur = []
                    dfs(i, j, cur)
                    paths.append(cur)
        
        count = 0
        for path in paths:
            flg = False
            for row, col in path:
                if not grid1[row][col]:
                    flg = True
                    break
            if not flg:
                count +=1 
                
        return count
        