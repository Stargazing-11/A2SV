class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        cond = False

        for i in range(len(arr)):
            if i == 0:
                continue
            if cond == False:
                if arr[i] < arr[i-1]:
                    if i <= 1:
                        return False
                    cond = True
                if arr[i] == arr[i -1]:
                    return False
            elif cond == True:
                if arr[i] >= arr[i-1]:
                    return False
        if cond == False:
            return False
        return True