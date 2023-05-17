# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        heap = []
        heapify(heap)

        for list_ in lists:
            while list_:
                heappush(heap, list_.val)
                list_ = list_.next
        
        sorted_list = ListNode()
        temp = sorted_list
        
        while heap:
            val = heappop(heap)
            temp.next = ListNode(val)
            temp = temp.next
        
        return sorted_list.next
                