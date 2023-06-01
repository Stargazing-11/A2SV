class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
    def addNum(self, num: int) -> None:
        if len(self.min_heap) == len(self.max_heap):
            heappush(self.min_heap, -num)
            popped = heappop(self.min_heap)
            heappush(self.max_heap, -popped)
        
        else:
            heappush(self.max_heap, num)
            popped = -heappop(self.max_heap)
            
            heappush(self.min_heap, popped)
        
    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return float(self.max_heap[0] - self.min_heap[0])/ 2
        return float(self.max_heap[0])


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()