
def insertionSort1(n, arr):
    x = 0
    for i in range(n):
        for j in range(n):
            x = n-j-1
            if n-2-j>=0 and(arr[x] < arr[x-1]):
                y=arr[x]  
                arr[x] = arr[n-2-j]
                print(*arr)
                arr[n-2-j] = y
    print(*arr)

    