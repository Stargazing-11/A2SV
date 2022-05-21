# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        ansList = ans
        out = []
        outof = []
        while(head):
            val1 = head.val
            out.append(val1)
            head = head.next
            
        for i in out:
            if i not in outof:
                outof.append(i)
        for i in outof:
            ansList.next = ListNode(i)
            ansList = ansList.next
        return ans.next