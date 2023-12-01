# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        ans = []
        def dfs(root):
            if not root:
                return 
            
            left = dfs(root.left)
            right = dfs(root.right)
            if root.val in to_delete:
                if left:
                    ans.append(left)
                if right:
                    ans.append(right)
                root = None
            
            if root:
                cur_root = TreeNode(root.val)
                cur_root.left = left
                cur_root.right = right
            else:
                return None
            return cur_root
        root = dfs(root)
        if root:
            ans.append(root)
        return ans 