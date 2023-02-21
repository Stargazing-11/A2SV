# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
            if not head:
                return head
        
            N = 1
            temp = head
            while temp.next:
                temp = temp.next
                N += 1
            
            c = 1
            temp = head
            if (k % N) == 0:
                return head
            while temp and c < (N - (k % N)):
                temp = temp.next
                c += 1
            
            new = temp.next
            temp.next = None
            temp = new
            while temp and temp.next:
                temp = temp.next
            
            temp.next = head
            head = new
            return head
                