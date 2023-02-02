class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        hashMap = defaultdict(list)

        for i, row in enumerate(matrix):
            for j, col in enumerate(row):
                hashMap[j].append(col)
        
        for key in hashMap.keys():
            temp = hashMap[key]
            temp.reverse()
            matrix[key] = temp
        