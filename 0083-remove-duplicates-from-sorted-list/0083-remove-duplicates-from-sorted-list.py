# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = defaultdict(int)
        
        temp = head
        ans = ListNode()
        prev = ans
        while temp:
            if count[temp.val] == 0:
                count[temp.val] += 1
                prev.next = ListNode(temp.val)
                prev = prev.next
            temp = temp.next
        return ans.next