# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        twin = {}
        temp = head
        maxSum = 0
        N = 0
        
        while temp:
            N += 1
            temp = temp.next
        
        temp = head
        counter = 0
        while temp:
            if counter in twin:
                maxSum = max(maxSum, twin[counter] + temp.val)
            twin[N-counter-1] = temp.val
            temp = temp.next
            counter += 1
        return maxSum