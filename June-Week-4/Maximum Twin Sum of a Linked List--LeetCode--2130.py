# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        leng = 0
        start = head
        nums = []
        while(start):
            leng += 1
            nums.append(start.val)
            start = start.next
        start = head
        twins = []
        for i, j in enumerate(nums):
            if 0 <= i <= (leng//2) - 1:
                x = nums[leng-1-i]
                twins.append([j, x])
        hold_sum = []
        for k in twins:
            hold_sum.append(k[0] + k[1])
        return max(hold_sum)