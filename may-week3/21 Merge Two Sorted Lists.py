import math
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        ansList = ans
        out = []
        while(list1):
            val1 = list1.val
            out.append(val1)
            list1 = list1.next
        while(list2):
            val2 = list2.val
            out.append(val2)
            list2 = list2.next
        out.sort()
        for i in out:
            ansList.next = ListNode(i)
            ansList = ansList.next
        return ans.next