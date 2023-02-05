# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return ListNode().next
        new = ListNode(head.val)
        temp = head.next
        while temp:
            temp2 = ListNode(temp.val)
            temp2.next = new
            new = temp2
            temp = temp.next
        return new