# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        string = [""]
        def dfs(root):
            
            string.append(str(root.val))
            
            if root.left:
                string.append("(")
                dfs(root.left)
            
            if root.right:
                if not root.left:
                    string.append("()")
                string.append("(")
                dfs(root.right)
                
            string.append(")")
            if not root.right and not root.left:
                return 
        
        dfs(root)
        string.pop()
        return "".join(string)