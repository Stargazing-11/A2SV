# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odds = ListNode()
        temp1 = odds
        evens = ListNode()
        temp2 = evens
        
        c = 1
        while head:
            if c % 2 != 0:
                temp1.next = ListNode(head.val)
                temp1 = temp1.next
            else:
                temp2.next = ListNode(head.val)
                temp2 = temp2.next
            head = head.next
            c += 1
            
        temp1.next = evens.next
        return odds.next