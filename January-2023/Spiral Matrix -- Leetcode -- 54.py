class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = matrix[0]
        matrix.pop(0)

        while matrix:
            matrix = list(map(list, zip(*matrix)))
            ans += matrix[-1]
            matrix.pop()
            matrix.reverse()
        return ans
