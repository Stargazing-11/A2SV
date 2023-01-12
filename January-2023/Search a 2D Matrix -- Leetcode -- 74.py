class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for row in matrix:
            if row[0] > target:
                return False

            if row[0] <= target <= row[-1]:
                left, right = 0, len(row)

                # if row[0] == target or row[-1] == target:
                #     return True

                while left < right:
                    mid = (left + right) // 2
                    if row[mid] > target:
                        right = mid
                    elif row[mid] < target:
                        left = mid + 1
                    else:
                        return True
                return False
