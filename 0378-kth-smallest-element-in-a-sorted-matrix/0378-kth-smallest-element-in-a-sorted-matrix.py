class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for i in range(len(matrix)):
            heap += matrix[i]
        
        heapq.heapify(heap)
        while k > 1:
            heapq.heappop(heap)
            k -= 1
        return heapq.heappop(heap)