# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ans, self.k = 0, k
        
        def findKth(root):
            if not root:
                return 
            
            findKth(root.left)
            self.k -= 1
            
            if self.k == 0:
                self.ans = root.val
                return
            findKth(root.right)
            return 
        findKth(root)
        return self.ans