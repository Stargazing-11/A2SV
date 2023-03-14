# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        
        depth = 1
        stk = []
        cur = root
        while cur or stk:
            while cur:
                stk.append((cur, depth))
                cur = cur.left
                depth += 1
            
            node, dpz = stk.pop()
            max_depth = max(max_depth, dpz)
            if node.right:
                cur = node.right
                depth = dpz + 1
        return max_depth