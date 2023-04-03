# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(root, min_max):
            if not root:
                return True
            if root.val <= min_max[0] or root.val >= min_max[1]:
                return False
            
            return validate(root.left, [min_max[0], root.val]) and validate(root.right, [root.val, min_max[1]])
        
        ans = validate(root, (float("-inf"), float("inf")))
        print(ans)
        return ans