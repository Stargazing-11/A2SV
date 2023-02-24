# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        temp = head
        nums = []
        
        while temp:
            nums.append(temp.val)
            temp = temp.next
        
        monStk = []
        ans = [0 for i in range(len(nums))]
        for i in range(len(nums)):
            while monStk and nums[monStk[-1]] < nums[i]:
                ans[monStk.pop()] = nums[i]
            monStk.append(i)
        return ans