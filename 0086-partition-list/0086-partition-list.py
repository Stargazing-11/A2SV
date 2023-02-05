# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head == None:
            return None
        less = ListNode()
        less2 = less
        large = ListNode()
        large2 = large
        temp = head
        while temp:
            if temp.val < x:
                less2.next = ListNode(temp.val)
                less2 = less2.next
            else:
                large2.next = ListNode(temp.val)
                large2 = large2.next
            temp = temp.next
        less2.next = large.next
        
        return less.next
                