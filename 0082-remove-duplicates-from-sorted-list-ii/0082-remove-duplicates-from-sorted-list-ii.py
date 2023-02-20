# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dic = defaultdict(int)
        temp = head
        
        while temp:
            dic[temp.val] += 1
            temp = temp.next
            
        ans = ListNode()
        temp = ans
        
        for key in dic.keys():
            if dic[key] < 2:
                temp.next = ListNode(key)
                temp = temp.next
        
        return ans.next