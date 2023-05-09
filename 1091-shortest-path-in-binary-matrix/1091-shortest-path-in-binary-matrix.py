class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        
        def inBound(r, c):
            return 0<= r < len(grid) and 0 <= c < len(grid[0])
        
        directions = [(0,1),(1,0),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]

        que = deque([((0, 0), 1)])
        visited = set((0, 0))

        while que:
            root, count = que.popleft()
            if root[0] == len(grid)-1 and root[1] == len(grid[0])-1:
                return count

            for r, c in directions:
                new_r, new_c = root[0] + r, root[1] + c

                if inBound(new_r, new_c) and (new_r, new_c) not in visited and grid[new_r][new_c] == 0:
                    visited.add((new_r, new_c))
                    que.append(((new_r, new_c), count + 1))

        return -1 