class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        
        not_flip = []
        
        for i in range(len(board[0])):

            if board[0][i] == "O":
                not_flip.append((0, i))
            
            if board[len(board) - 1][i] == "O":
                not_flip.append((len(board)-1, i))
       
        for i in range(len(board)):

            if board[i][0] == "O" and i != 0 and i != len(board) -1:
                not_flip.append((i, 0))
            
            if board[i][len(board[0]) - 1] == "O" and i != 0 and i != len(board) -1:
                not_flip.append((i, len(board[0])-1))      

        def inBound(row, col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])

        visited = set()            
        def dfs(row, col):
            visited.add((row, col))
            
            for r, c in directions:
                new_r, new_c = row + r, col + c
                
                if inBound(new_r, new_c) and (new_r, new_c) not in visited and board[new_r][new_c] == "O":
                    dfs(new_r, new_c)

        for row, col in not_flip:
            dfs(row, col)

        for i in range(len(board)):
            for j in range(len(board[0])): 
                if board[i][j] == "O" and (i, j) not in visited:
                    board[i][j] = "X"
        
        
        