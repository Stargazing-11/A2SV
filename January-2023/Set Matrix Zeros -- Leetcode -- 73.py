class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeros = defaultdict(set)

        for index, row in enumerate(matrix):
            for ind, col in enumerate(row):
                if col == 0:
                    zeros[0].add(index)
                    zeros[1].add(ind)

        for i in zeros[0]:
            matrix[i] = [0 for k in range(len(matrix[0]))]

        for row in matrix:
            for j in zeros[1]:
                row[j] = 0
