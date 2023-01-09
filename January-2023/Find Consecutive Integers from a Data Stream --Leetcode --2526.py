class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.stream = []
        self.falses = 0

    def consec(self, num: int) -> bool:
        self.stream.append(num)

        if num != self.value:
            self.falses += 1

        if len(self.stream) > self.k:
            temp = self.stream[0]
            self.stream = self.stream[1:]

            if temp != self.value:
                self.falses -= 1
        elif len(self.stream) < self.k:
            return False
        return self.falses == 0


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
