# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        levels = defaultdict(list)
        
        def travers(root, level):
            if not root:
                return 
            
            levels[level].append(root.val)
            travers(root.left, level+1)
            travers(root.right, level+1)
        travers(root, 0)
        return [values[-1] for values in levels.values()]