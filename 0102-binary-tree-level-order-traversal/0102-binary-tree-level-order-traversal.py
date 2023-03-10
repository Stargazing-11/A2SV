# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = defaultdict(list)
        
        def levelTraversal(root, level):
            if not root:
                return 
            
            levels[level].append(root.val)
            
            levelTraversal(root.left, level+1)
            levelTraversal(root.right, level+1)
        
        levelTraversal(root, 0)
        return levels.values()