# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left, right = head, head
        
        while right and right.next:
            right = right.next.next
            left = left.next
        
        ans = ListNode(left.val)
        temp = ans
        left = left.next
        while left:
            temp.next = ListNode(left.val)
            left = left.next
            temp = temp.next
        return ans