# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        start = head
        nums = []
        while(start):
            nums.append(start.val)
            start = start.next
        stac = []
        output = [0 for i in nums]
        count = 0
        for j,i in enumerate(nums):
            if not stac:
                stac.append([i,j])
                count += 1
            else:
                if stac[-1][0] < i:
                    while(stac and stac[-1][0] < i):
                        z = (stac.pop())
                        output[z[1]] = i
                    stac.append([i, j])
                else:
                    stac.append([i,j])
        return output