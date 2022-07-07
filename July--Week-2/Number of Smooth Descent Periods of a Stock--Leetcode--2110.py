class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 1
        temp = 1
        result = 1
        for i in range(1,len(prices)):
            if prices[i - 1] - prices[i] == 1:
                temp += 1 
            else: 
                temp = 1
            result += temp
        return result