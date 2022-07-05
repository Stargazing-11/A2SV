# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        start = head 
        nums = []
        
        while(start):
            nums.append(start.val)
            start = start.next
        
        left = 0
        
        while(left + k <= len(nums)):
            newnum = nums[left:left + k]
            newnum.reverse()
            nums[left:left + k] = newnum
            left += k
        
        head = ListNode()
        start = head
        
        for i in nums:
            start.next = ListNode(i)
            start = start.next
        return head.next