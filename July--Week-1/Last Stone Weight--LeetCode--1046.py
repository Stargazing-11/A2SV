class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        
        while(stones):
            stones.sort()
            if len(stones) == 1:
                return stones[0]
            x = stones.pop()
            y = stones.pop()
            
            if x != y:
                x = x - y
                stones.append(x)
        return 0