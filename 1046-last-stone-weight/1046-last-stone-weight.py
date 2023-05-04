class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1 *( stone) for stone in stones]
        heapify(stones)
        
        while len(stones) > 1:
            first = heappop(stones) * -1 
            second = heappop(stones) * -1 
            
            diff = abs(first - second)
            
            heappush(stones, diff * -1)
        return stones[0] * -1  