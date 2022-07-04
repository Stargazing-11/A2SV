from functools import reduce

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pass
        nums = []
        for i in lists:
            start = i
            x = []
            while(start):
                x.append(start.val)
                start = start.next
            if x:
                nums.append(x)
        if not nums:
            head = ListNode()
            return head.next
        single_list = reduce(lambda x,y: x+y, nums)
        single_list.sort()
        head = ListNode(0)
        start = head
        
        for i in single_list:
            start.next = ListNode(i)
            start = start.next
        return head.next