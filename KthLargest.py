class Solution:
    def kthLargestNumber(self, arr: List[str], k: int) -> str:
        for i in range(len(arr)):
            arr[i] = int(arr[i])
        Solution.mergeSort(arr)
        return str(arr[-k])
    def mergeSort(arr):
        if len(arr) > 1:
            mid = len(arr)//2
            L = arr[:mid]
            R = arr[mid:]
            Solution.mergeSort(L)
            Solution.mergeSort(R)
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
        return arr