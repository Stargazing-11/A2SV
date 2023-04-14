class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        digits = defaultdict(list)

        def check(col, i, j):
            if col in digits["c"+str(i)]:
                return False
            if col in digits["r"+str(j)]:
                return False
            if col in digits[str(i//3)+str(j//3)]:
                return False
            return True

        for i, row in enumerate(board):
            for j, col in enumerate(row):
                if col == ".":
                    continue
                if not check(col, i, j):
                    return False
                else:
                    digits["c" + str(i)].append(col)
                    digits["r" + str(j)].append(col)
                    digits[str(i//3) + str(j//3)].append(col)
        return True
        