class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        dif = [prices[i] - prices[i-1] for i in range(1, len(prices))]
        
        return sum([elem for elem in dif if elem > 0])