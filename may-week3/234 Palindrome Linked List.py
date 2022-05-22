# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l = []
        while(head):
            l.append(head.val)
            head = head.next
        print(l)
        
        k = len(l)//2
        print(k)
        l1, l2 = [], []
        if len(l)%2 ==0:
            for i in l[:k]:
                l1.append(i)
            for i in l[k:]:
                l2.append(i)
            print(l1, l2)
        else:
            for i in l[:k]:
                l1.append(i)
            for i in l[k+1:]:
                l2.append(i)
            print(l1, l2)
        l2.reverse()
        print(l2)
        if l1 == l2:
            return True
        else:
            return False