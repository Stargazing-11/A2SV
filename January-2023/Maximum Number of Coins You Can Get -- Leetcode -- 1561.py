class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()

        maxPiles = 0

        left, right = 0, len(piles) - 2

        while left < right:
            maxPiles += piles[right]
            left += 1
            right -= 2
        return maxPiles
