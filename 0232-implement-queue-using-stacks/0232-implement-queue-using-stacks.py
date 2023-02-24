class MyQueue:

    def __init__(self):
        self.stk = []
        self.stk2 = []

    def push(self, x: int) -> None:
        self.stk.append(x)
        
        if not self.stk2:
            self.stk2.append(x)
        else:
            temp = []
            while self.stk2:
                temp.append(self.stk2.pop())
            temp.append(x)
            
            for i in temp[::-1]:
                self.stk2.append(i)

    def pop(self) -> int:
        return self.stk2.pop()

    def peek(self) -> int:
        return self.stk2[-1]

    def empty(self) -> bool:
        return len(self.stk2) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()