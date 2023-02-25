class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        monStk = []
        profit = 0
        for price in prices:
            while monStk and monStk[-1] > price:
                monStk.pop()
            monStk.append(price)
            profit = max(profit, monStk[-1] - monStk[0])
        return profit