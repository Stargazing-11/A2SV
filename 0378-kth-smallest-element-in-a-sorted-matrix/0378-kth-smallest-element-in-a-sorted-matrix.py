class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        heapify(heap)
        k = len(matrix) ** 2 - k + 1

        for row in matrix:
            for col in row:
                heappush(heap, col)
                if len(heap) > k:
                    heappop(heap)
        return heap[0]