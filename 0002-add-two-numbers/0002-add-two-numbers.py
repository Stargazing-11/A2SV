# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        totalSum = ""
        carry = 0
        def add(head1, head2, carry):
            nonlocal totalSum
            num = -1
            
            if head1 and head2:
                temp = (head1.val + head2.val + carry)
                num = 0
            elif head1 and not head2:
                temp = (head1.val + carry)
                num = 1
            elif head2 and not head1:
                temp = (head2.val + carry)
            else:
                if carry > 0:
                    totalSum += str(carry)
                return
            if temp >= 10:
                carry = temp // 10
                temp = temp % 10
            else:
                carry = 0
            totalSum += str(temp)  
            
            if num == 0:
                add(head1.next, head2.next, carry)
            elif num == 1:
                add(head1.next, head2, carry)
            else:
                add(head1, head2.next, carry)
                    
        add(l1, l2, carry)
        head = ListNode()
        
        def build(head, pos):
            if pos >= len(totalSum):
                return 
            head.next = ListNode(int(totalSum[pos]))
            head = head.next
            build(head, pos + 1)
        build(head, 0)
        return head.next