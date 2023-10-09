# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        ans = None
        def dfs(root, p, q):
            nonlocal ans
            
            if not root:
                return
            
            cur = False
            
            if root == p or root == q:
                cur = True
                
            if dfs(root.left, p, q):
                if cur :
                    ans = root
                cur = True
            
            if ans:
                return  
            
            if dfs(root.right, p, q):
                if cur :
                    ans = root
                cur = True
            
            return cur
        
        dfs(root, p, q)
        return ans 