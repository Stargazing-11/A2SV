class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        length = len(board)
        board.reverse()
        def getPos(pos):
            r = (pos -1) // length
            c = (pos - 1) % length
            
            if r % 2:
                c = length - 1 - c
            return [r, c]
        
        que = deque()
        visited = set()
        que.append([1, 0])
        
        
        while que:
            pos, moves = que.popleft()
            
            for i in range(1, 7):
                nextPos = pos + i
                r, c = getPos(nextPos)
                
                if board[r][c] != -1:
                    nextPos = board[r][c]

                if nextPos == length * length:
                    return moves + 1
                
                if nextPos not in visited:
                    visited.add(nextPos)
                    que.append([nextPos, moves + 1])
                    
        return -1 