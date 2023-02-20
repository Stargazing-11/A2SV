# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        N = 0
        
        while temp:
            temp = temp.next
            N += 1
        count = 0
        ans = ListNode()
        
        temp = ans
        while head:
            if count >= N//2:
                temp.next = ListNode(head.val)
                temp = temp.next
            count += 1
            head = head.next
        
        return ans.next