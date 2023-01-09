class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        o = "".join(board).count("O")
        x = "".join(board).count("X")

        if x > o + 1:
            return False
        if o > x:
            return False

        cols = defaultdict(str)

        for ind, row in enumerate(board):
            for index, value in enumerate(row):
                cols[index] += value

        diag1 = board[0][0] + board[1][1] + board[2][2]
        diag2 = board[0][2] + board[1][1] + board[2][0]
        board = set(board + list(cols.values()))
        board.add(diag1)
        board.add(diag2)
        if "XXX" in board and "OOO" in board:
            return False
        if "XXX" in board and x != o + 1:
            return False
        if "OOO" in board and o != x:
            return False
        return True
