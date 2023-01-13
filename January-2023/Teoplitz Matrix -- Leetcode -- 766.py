class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        diagElements = defaultdict(list)

        for index, row in enumerate(matrix):
            for ind, col in enumerate(row):
                if not diagElements[index - ind]:
                    diagElements[index - ind].append(col)
                elif diagElements and diagElements[index - ind][0] != col:
                    return False
        return True
