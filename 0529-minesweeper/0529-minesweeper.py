class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        row, col = click
        if board[row][col] == "M":
            board[row][col] = "X"
            return board
        
        directions = [(-1,0),(0,-1),(-1,-1),(1,1),(0,1),(1,0),(-1,1),(1,-1)]
        def isBound(row, col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])
        
        visited = set()
        
        def hasMine(row, col):
            count = 0
            for r, c in directions:
                new_r, new_c = row + r, col + c
                
                if isBound(new_r, new_c) and board[new_r][new_c] == "M":
                    count += 1
            return count
                
        def dfs(row, col):
            if (row, col) in visited:
                return 
            
            visited.add((row, col))
            count = hasMine(row, col)

            if count:
                board[row][col] = str(count)
                return 
            else:
                board[row][col] = "B"
                for r, c in directions:
                    new_r, new_c = row + r, col + c
                    if isBound(new_r, new_c) and (new_r, new_c) not in visited:
                        dfs(new_r, new_c)

        dfs(row, col)
        return board