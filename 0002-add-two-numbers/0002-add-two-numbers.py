# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = [], []
        
        temp = l1
        while temp:
            num1.append(str(temp.val))
            temp = temp.next
        
        temp = l2
        while temp:
            num2.append(str(temp.val))
            temp = temp.next
        num1.reverse()
        num2.reverse()
        
        num3 = str(int(''.join(num1)) + int(''.join(num2)))
        
        ans = ListNode()
        temp = ans
        
        for i in num3[::-1]:
            temp.next = ListNode(int(i))
            temp = temp.next
        return ans.next