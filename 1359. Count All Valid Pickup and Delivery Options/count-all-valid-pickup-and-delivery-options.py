class Solution:
    def countOrders(self, n: int) -> int:
        return factorial(2*n)//pow(2,n) % (1000000000 + 7)