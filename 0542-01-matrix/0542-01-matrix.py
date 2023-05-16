class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        
        def inBound(r, c):
            return 0 <= r < len(mat) and 0 <= c < len(mat[0])
        
        visited = set()
        que = deque([])
        
        for i in range(len(mat)):
            for j, val in enumerate(mat[i]):
                if val == 0:
                    visited.add((i, j))
                    que.append((i, j))

        
        while que:
            node = que.popleft()

            for r, c in directions:
                new_r, new_c = node[0] + r, node[1] + c

                if inBound(new_r, new_c) and (new_r, new_c) not in visited:
                    que.append((new_r, new_c))
                    cur = mat[node[0]][node[1]] 
                    mat[new_r][new_c] += cur
                    visited.add((new_r, new_c))
        return mat