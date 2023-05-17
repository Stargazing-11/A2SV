class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (0, 1), (-1, 0),(0, -1)]
        
        def inBound(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])
        
        que = deque([])
        visited = set()
        
        def findConnectedOnes(node):
            visited.add(node)
            que.append((node, 0))
            row, col = node
            
            for r, c in directions:
                new_r, new_c = row + r, col + c
                
                if inBound(new_r, new_c) and (new_r, new_c) not in visited and grid[new_r][new_c]:
                    findConnectedOnes((new_r, new_c))
        
        found = False
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if col:
                    found = True
                    findConnectedOnes((i, j))
                    break
            if found:
                break

        while que:
            node, distance = que.popleft()
            
            for r, c in directions:
                new_r, new_c = node[0] + r, node[1] + c
                
                if inBound(new_r, new_c) and (new_r, new_c) not in visited:
                    if grid[new_r][new_c] == 1:
                        return distance
                    visited.add((new_r, new_c))
                    que.append(((new_r, new_c), distance + 1))
        