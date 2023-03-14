# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        ans = []
        stk = []
        cur = root
        
        while stk or cur:
            while cur:
                stk.append(cur)
                cur = cur.left
            
            cur = stk.pop()
            ans.append(cur.val)
            cur = cur.right
        return ans 