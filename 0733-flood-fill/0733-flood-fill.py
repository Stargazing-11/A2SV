class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        default = image[sr][sc]
        visited = set()
        def inBound(row, col):
            return 0 <= row < len(image) and 0 <= col < len(image[0])
        
        def dfs(row, col):
            visited.add((row, col))
            image[row][col] = color
            
            for r, c in directions:
                new_row = row + r
                new_col = col + c
                
                if inBound(new_row, new_col) and (new_row, new_col) not in visited and image[new_row][new_col] == default:
                    dfs(new_row, new_col)
        
        dfs(sr, sc)
        return image