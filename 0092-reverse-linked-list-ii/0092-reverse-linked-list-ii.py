# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        temp = head
        
        counter = 1
        
        while temp:
            if counter == left:
                temp2 = ListNode()
                
                while counter <= right:
                    new = ListNode(temp.val)
                    new.next = temp2
                    temp2= new
                    counter += 1
                    temp = temp.next
                break
            temp = temp.next
            counter += 1
        tem = temp2
        
        while tem.next.next:
            tem = tem.next
        tem.next = temp
        
        if left == 1:
            return temp2
        c = 1
        temp = head

        while c < left-1:
            temp = temp.next
            c += 1
        temp.next = temp2
        return head