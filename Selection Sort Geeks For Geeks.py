class Solution: 
    def select(self, arr, i):
        for k in range(len(arr)):
            if arr[k] < arr[i]:
                arr[k], arr[i]=arr[i],arr[k]
    def selectionSort(self, arr,n):
        for j in range(n):
            min = j

            for i in range(j + 1, n):
    
                if arr[i] < arr[min]:
                    min = i
    
            (arr[j], arr[min]) = (arr[min], arr[j])