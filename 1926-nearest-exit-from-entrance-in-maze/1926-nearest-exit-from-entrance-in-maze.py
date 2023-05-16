class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        def inBound(r, c):
            return 0 <= r < len(maze) and 0 <= c < len(maze[0]) and maze[r][c] != "+"
        
        def isExit(r, c):
            return r + 1 >= len(maze) or r - 1 < 0 or c + 1 >= len(maze[0]) or c - 1 < 0
        
        directions = [(0, 1), (1, 0), (-1 ,0), (0, -1)]
        
        que = deque([])
        que.append((entrance[0], entrance[1]))
        maze[entrance[0]][entrance[1]] = 0
        
        visited = set()
        visited.add((entrance[0], entrance[1]))
        while que:
            row, col = que.popleft()
            
            for r, c in directions:
                new_r, new_c = row + r, col + c

                if inBound(new_r, new_c) and (new_r, new_c) not in visited:
                    if maze[new_r][new_c] == ".":
                        maze[new_r][new_c] = maze[row][col] + 1
                        
                        if isExit(new_r, new_c):
                            return maze[new_r][new_c]
                        
                        que.append((new_r, new_c))
                        visited.add((new_r, new_c))
                        
        return -1