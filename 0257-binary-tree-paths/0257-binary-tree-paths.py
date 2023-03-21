# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        output = []
        
        def path(root, cur, output):
            if not root.left and not root.right:
                output.append(cur.copy())
                return 
            
            if root.left:
                cur.append(str(root.left.val))
                path(root.left, cur, output)
                cur.pop()
            
            if root.right:
                cur.append(str(root.right.val))
                path(root.right, cur, output)
                cur.pop()
        
        path(root, [str(root.val)], output)
        return ["->".join(paz) for paz in output]