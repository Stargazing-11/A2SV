class DataStream:

    def __init__(self, value: int, k: int):
        self.stream = []
        self.value = value
        self.k = k

    def consec(self, num: int) -> bool:
        if num != self.value:
            self.stream.clear()
            return False
        self.stream.append(num)
        
        if len(self.stream) >= self.k:
            return True
    


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)