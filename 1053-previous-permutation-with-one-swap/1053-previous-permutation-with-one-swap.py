class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)

        right_big = arr[-1]
        valley = (float('inf'), -1)
        
        for i in range(n-2, -1, -1):
            if arr[i] <= right_big:
                right_big = arr[i]
            else:
                valley = (arr[i], i)
                break
        if valley[0] == float('inf'):
            return arr
        
        swap = (float('-inf'), -1) 
        
        for i in range(n-1, valley[1]-1, -1):
            if arr[i] < valley[0] and arr[i] >= swap[0]:
                swap = (arr[i], i)
        
        if swap[0] == float('-inf'):
            return arr
        
        arr[swap[1]], arr[valley[1]] = arr[valley[1]], arr[swap[1]]
        
        return arr