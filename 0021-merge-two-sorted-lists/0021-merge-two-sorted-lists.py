# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        temp = ans
        def merge(list1, list2, ans):
            if list1 == None and list2 == None:
                return ans
            
            if list1 and list2 and list1.val <= list2.val or list1 and not list2:
                ans.next = ListNode(list1.val)
                list1 = list1.next
            elif list1 and list2 and list1.val > list2.val or list2 and not list1:
                ans.next = ListNode(list2.val)
                list2 = list2.next
            ans = ans.next
            return merge(list1, list2, ans)
        merge(list1, list2, temp)
        return ans.next