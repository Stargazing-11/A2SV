class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        max_size = 0
        j = 0
        piles.sort()
        piles.reverse()
        for i in range(1,len(piles),2):
            max_size += piles[i]
            j += 1
            if j == len(piles)//3:
                return max_size
        return max_size