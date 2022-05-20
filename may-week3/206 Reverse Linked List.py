# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        ansList = ans
        out = []
        while(head):
            temp = ListNode(head.val)
            temp.next = ansList
            ansList = temp
            head = head.next
        while(ansList.next):
            out.append(ansList.val)
            ansList = ansList.next
        ans = ListNode(0)
        ansList = ans
        for i in out:
            ansList.next = ListNode(i)
            ansList = ansList.next
        print(ans.next)
        return ans.next