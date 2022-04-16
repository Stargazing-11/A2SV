from collections import deque
class MyCircularDeque:
    def __init__(self, k: int):
        self.queue = deque([], maxlen = k)
        print(self.queue, "init")
        self.lengthe = k
    def insertFront(self, value: int) -> bool:
        if len(self.queue) == self.lengthe:
            return False
        self.queue.appendleft(value)
        return True
    def insertLast(self, value: int) -> bool:
        if len(self.queue) == self.lengthe:
            return False
        self.queue.append(value)
        print(self.queue, "is full")
        return True
    def deleteFront(self) -> bool:
        if len(self.queue) == 0:
            return False
        self.queue.popleft()
        return True
    def deleteLast(self) -> bool:
        if len(self.queue) == 0:
            return False
        self.queue.pop()
        return True
    def getFront(self) -> int:
        print(self.queue, "get front")
        if len(self.queue) == 0:
            return -1
        return self.queue[0]
    def getRear(self) -> int:
        print(self.queue, "get rear")
        if len(self.queue) == 0:
            return -1
        return self.queue[-1]

    def isEmpty(self) -> bool:
        print(self.queue, "is empty")
        return len(self.queue)==0

    def isFull(self) -> bool:
        print(len(self.queue), self.lengthe, "is full")
        return len(self.queue) == self.lengthe


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()