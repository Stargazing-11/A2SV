class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        ans = []
        temp = []

        for index, row in enumerate(mat):
            for ind, col in enumerate(row):
                temp.append(col)
                if len(temp) == c:
                    ans.append(temp)
                    temp = []
        if len(ans) == r and len(ans[0]) == c:
            return ans
        return mat