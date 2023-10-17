# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverseLinkedList(head):
            reversedList = ListNode(head.val)
            temp = head.next
            while temp:
                temp2 = ListNode(temp.val)
                temp2.next = reversedList
                reversedList = temp2
                temp = temp.next
            return reversedList
        
        def addNumbers(l1, l2):
            carry, total = 0,0
            newList = ListNode()
            temp = newList
            
            while l1 or l2:
                if l1:
                    total += l1.val
                    l1 = l1.next
                if l2:
                    total += l2.val
                    l2 = l2.next
                
                temp.next = ListNode(total % 10)
                carry = total // 10
                temp = temp.next
                total = carry
            if carry:
                temp.next = ListNode(carry)
                temp = temp.next
            return newList.next
        l1 = reverseLinkedList(l1)        
        l2 = reverseLinkedList(l2)

        addNumber = addNumbers(l1, l2)
        return reverseLinkedList(addNumber)
        