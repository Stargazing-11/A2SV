# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def pathSum(root, curSum):
            if not root:
                return 
            if not root.left and not root.right:
                if curSum + root.val == targetSum:
                    return True
                return False
            
            leftPath = pathSum(root.left, curSum + root.val)
            rightPath = pathSum(root.right, curSum + root.val)
            
            return leftPath or rightPath
        return pathSum(root, 0)