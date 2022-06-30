# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    x = ListNode()
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        x = ListNode()
        k = x
        start = head
        count = 0
        while(start):
            i = start.val
            start = start.next
            count += 1
            if not start:
                k.next = ListNode(i)
                break
                
            j = start.val
            i, j = j, i
            
            y = ListNode(i)
            z = ListNode(j)
            
            k.next = y
            y.next = z
            k = z
            start = start.next
        return x.next