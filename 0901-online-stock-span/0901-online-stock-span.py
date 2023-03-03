class StockSpanner:

    def __init__(self):
        self.monStk = []
        self.count = 0

    def next(self, price: int) -> int:
        while self.monStk and self.monStk[-1][1] <= price:
            self.monStk.pop()
            
        if not self.monStk:
            self.monStk.append([self.count, price])
            self.count += 1
            return self.count
        
        ans = self.count - self.monStk[-1][0]
        self.monStk.append([self.count, price])
        self.count += 1
        return ans 

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)