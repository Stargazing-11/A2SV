class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []
        for pile in piles:
            heap.append(-pile)
        
        heapify(heap)
        
        for i in range(k):
            val = (heappop(heap)) * -1 
            val -= val // 2
            heappush(heap, -1 * val)
        
        return sum(heap) * -1