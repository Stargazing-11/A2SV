class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        #check_unique_elements
        def is_unique(r, c):
            elem = set()
            for i in range(r, r+3):
                for j in range(c, c + 3):
                    if grid[i][j] in elem:
                        return False
                    elem.add(grid[i][j])
            return True
        
        #check_bound
        def inBound(r, c):
            return 0 <= r+3 <= len(grid) and 0 <= c+3 <= len(grid[0]) 
        
        #check_range(1, 9)
        def is_in_range(r, c):
            for i in range(r, r+3):
                for j in range(c, c + 3):
                    if 1 > grid[i][j] or 9 < grid[i][j]:
                        return False
            return True
        
        
        def check_sum(r, c):
            if not is_unique(r, c) or not is_in_range(r, c):
                return False
            
            new = [grid[i][c:c+3].copy() for i in range(r, r+3)]
            check = sum(new[0])
            
            # check row sum   
            col_sum = {}
            for i in range(3):
                if sum(new[i]) != check:
                    return False
                
                col_sum[0] = col_sum.get(0, 0) + new[i][0]
                col_sum[1] = col_sum.get(1, 0) + new[i][1]
                col_sum[2] = col_sum.get(2, 0) + new[i][2]
                
            # check col sum
            for i in range(3):
                if col_sum[i] != check:
                    return False
            #diagonal sum 1
            if new[0][0] + new[1][1] + new[2][2] != check:
                return False
            # diagonal sum 2
            if new[0][2] + new[1][1] + new[2][0] != check:
                return False
            return True

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if inBound(i, j):
                    if check_sum(i, j):
                        count += 1
        return count