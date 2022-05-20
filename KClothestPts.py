import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        y = []
        for i in range(len(points)):
            x = Solution.dist(points[i])
            points[i].insert(0,x)
        print(points)
        
        points = Solution.mergeSort(points)
        for n in range(k):
            y.append(points[n][1:])
        return y
    
    def mergeSort(arr):
        if len(arr) > 1:
            mid = len(arr)//2
            L = arr[:mid]
            R = arr[mid:]
            Solution.mergeSort(L)
            Solution.mergeSort(R)
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i][0] < R[j][0]:
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
    def dist(pts):
        dis = pts[0] **2 + pts[1]**2
        dista = math.sqrt(dis)
        return dista