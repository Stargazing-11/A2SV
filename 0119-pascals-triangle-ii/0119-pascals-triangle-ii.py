class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        rowBefore = self.getRow(rowIndex-1)
        
        new = []
        for i in range(rowIndex+1):
            if i == 0 or i == rowIndex:
                new.append(1)
            else:
                new.append(rowBefore[i] + rowBefore[i-1])
        return new