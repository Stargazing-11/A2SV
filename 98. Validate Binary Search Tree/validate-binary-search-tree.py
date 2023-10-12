# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(root, max_, min_):
            if not root:
                return True
            
            if not (min_ < root.val < max_):
                return False
            
            right = validate(root.right, max_, root.val)
            left = validate(root.left, root.val, min_)
            
            return left and right
        
        left = validate(root.left, root.val, float('-inf'))
        right = validate(root.right, float('inf'), root.val)
        
        return left and right 