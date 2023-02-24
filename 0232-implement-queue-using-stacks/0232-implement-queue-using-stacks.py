class MyQueue:

    def __init__(self):
        self.stk = []
        self.right = 0

    def push(self, x: int) -> None:
        self.stk.append(x)

    def pop(self) -> int:
        val = self.stk[self.right]
        self.right += 1
        return val

    def peek(self) -> int:
        return self.stk[self.right]

    def empty(self) -> bool:
        return len(self.stk) == self.right


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()