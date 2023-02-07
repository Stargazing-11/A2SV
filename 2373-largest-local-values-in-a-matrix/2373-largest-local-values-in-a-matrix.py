class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        arr = []
        
        for i in range(len(grid) - 2):
            temp = []
            for j in range(len(grid) - 2 ):
                big = 0
                for k in range(i, i+3):
                    big = max(big, max(grid[k][j:j+3]))
                temp.append(big)
            arr.append(temp)
        return arr