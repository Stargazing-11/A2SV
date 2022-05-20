import array 
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        arr = array.array('i',nums)
        x = []

        for j in range(len(arr)):
            min = j
            for i in range(j + 1, len(arr)):
    
                if arr[i] < arr[min]:
                    min = i
            (arr[j], arr[min]) = (arr[min], arr[j])
        for k in range(len(arr)):
            if arr[k] == target:
                x.append(k)
        return x