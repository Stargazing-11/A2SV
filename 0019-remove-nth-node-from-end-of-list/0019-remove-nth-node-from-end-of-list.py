# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N = 0
        
        temp = head
        
        while temp:
            temp = temp.next
            N += 1
        if N == 1:
            return None
        temp = head
        count = 0
        ans = ListNode()
        temp2 = ans
        while count < N-n:
            temp2.next = ListNode(temp.val)
            temp2 = temp2.next
            temp = temp.next
            count += 1

        temp = temp.next
        temp2.next = temp
        return ans.next