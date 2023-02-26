class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        
        for col_ind in range(len(strs[0])):
            found = False
            for row_ind in range(1, len(strs)):
                if found == False and ord(strs[row_ind][col_ind]) < ord(strs[row_ind -1][col_ind]):
                    count += 1
                    found = True
        return count