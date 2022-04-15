class MinStack:

    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        return self.stack.append(val)
    def pop(self) -> None:
        return self.stack.pop()
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        mini = self.stack[0]
        for i in self.stack:
            if i < mini:
                mini = i
        return mini


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()