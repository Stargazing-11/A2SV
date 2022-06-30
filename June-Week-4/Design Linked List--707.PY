class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        nodes = self.head
        counter = 0
        while(nodes):
            if counter == index:
                return nodes.val
            nodes = nodes.next
            counter += 1
        return -1

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.head
        self.head = newNode
        nums = []
        new = self.head
        while(new):
            nums.append(new.val)
            new = new.next        
    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)
        nodes = self.head
        if self.head is None:
            self.head = newNode
        else:
            while(nodes.next):
                nodes = nodes.next
            nodes.next = newNode
        nums = []
        new = self.head
        while(new):
            nums.append(new.val)
            new = new.next
    def addAtIndex(self, index: int, val: int) -> None:
        newNode = ListNode(val)
        nodes = self.head
        counter = 1
        if index == 0:
            self.addAtHead(val)
        else:
            while(nodes):
                if counter == index:
                    temp = nodes.next
                    nodes.next = newNode
                    newNode.next = temp
                    break
                counter += 1
                nodes = nodes.next
        nums = []
        new = self.head
        while(new):
            nums.append(new.val)
            new = new.next
    def deleteAtIndex(self, index: int) -> None:
        nodes = self.head
        if index == 0:
            temp = self.head
            self.head = temp.next
        else:
            counter =  1
            while(nodes):
                if counter == index:
                    if nodes.next == None:
                        break
                    temp = nodes.next
                    nodes.next = temp.next
                nodes = nodes.next
                counter += 1
        nums = []
        new = self.head
        while(new):
            nums.append(new.val)
            new = new.next
        
#,"addAtIndex","deleteAtIndex","addAtHead","addAtTail","get","addAtHead","addAtIndex","addAtHead" ,[3,0],[2],[6],[4],[4],[4],[5,0],[6]
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)