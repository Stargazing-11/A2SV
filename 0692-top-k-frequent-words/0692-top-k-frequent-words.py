class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counted = Counter(words)
        heap = []
        
        for key in counted.keys():
            heap.append((-1 * counted[key], key))
            
        heapify(heap)
        ans = []
        for i in range(k):
            popped = heappop(heap)
            ans.append(popped[1])
        return ans