class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        heapify(heap)
        
        for stone in stones:
            heappush(heap, -1 * stone)

        while len(heap) > 1:
            y = -1 * (heappop(heap))
            x = -1 * (heappop(heap))
            if x != y:
                y -= x
                heappush(heap, -1 * y)
        return heap[0] * -1 if heap else 0