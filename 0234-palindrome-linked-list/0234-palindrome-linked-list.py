# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        
        temp = head
        
        leng = 0 
        while temp:
            temp = temp.next
            leng += 1
            
        count = 0
        temp = head
        while count < leng//2:
            arr.append(temp.val)
            temp = temp.next
            count += 1
        count = 1    
        if leng % 2 != 0:
            temp = temp.next

        while temp:
            if arr[-count] != temp.val:
                return False
            temp = temp.next
            count += 1
        return True