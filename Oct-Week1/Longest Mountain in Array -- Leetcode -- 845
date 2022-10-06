class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        if len(arr) < 3:
            return 0
        answer = 0
        left, right, cond, count = 0, 1, False, 1
        
        while right < len(arr):
            # print(arr[right], answer, count)
            if arr[right] < arr[right - 1] and cond == False:
                if arr[right -1] > arr[left]:
                    cond = True
                    count += 1
                else:
                    left = right
                    if count >= 3:
                        answer = max(answer, count)
                    count = 1
            elif arr[right] < arr[right - 1] and cond == True:
                count += 1
            elif arr[right] >= arr[right - 1] and cond == True:
                if count >= 3:
                    answer = max(answer, count)
                if arr[right - 1] < arr[right]:
                    left = right - 1
                    count = 2
                else:
                    left = right
                    count = 1
                cond = False
            elif arr[right] > arr[right -1] and cond == False:
                count += 1
            else:
                left = right
                if count >= 3 and cond == True:
                    answer = max(answer, count)
                count = 1
                cond = False
            right += 1
        if count >= 3 and cond == True:
            answer = max(answer, count)
        return answer