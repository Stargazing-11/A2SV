# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        count = [0]
        def dfs(root, cur):
            if not root:
                return 
            
            if len(cur) >= 2:
                if cur[-2] % 2 == 0:
                    count[0] += root.val
                    
            cur.append(root.val)
            dfs(root.left, cur)
            dfs(root.right, cur)
            cur.pop()
        
        dfs(root, [])
        
        return count[0]