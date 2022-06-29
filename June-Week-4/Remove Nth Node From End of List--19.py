# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        leng = 0
        self.start = head
        newhead = ListNode()
        while(self.start):
            leng += 1
            self.start = self.start.next
        count = 0
        self.start = head
        newnewhead = newhead
        while(self.start):
            if count == leng - n:
                self.start = self.start.next
                count += 1
                continue
            else:
                newnewhead.next = ListNode(self.start.val)
                newnewhead = newnewhead.next
            self.start = self.start.next
            count += 1
        return newhead.next