# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        ansList = ans
        out = []
        outof = []
        while(head):
            val = head.val
            val1 = head.val
            out.append(val1)
            head = head.next
        out.sort()
        for i in out:
            ansList.next = ListNode(i)
            ansList = ansList.next
        return ans.next