class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        left, right = 0, k
        count = 0
        temp = arr[left:right]
        total = sum(temp)
        average = total/k
        if average >=threshold:
            count += 1
        right += 1
        left += 1
        
        while right <= len(arr):
            total += (arr[right-1] - arr[left-1])
            average = total / k 
            if average >= threshold:
                count += 1
            right += 1
            left += 1
        return count