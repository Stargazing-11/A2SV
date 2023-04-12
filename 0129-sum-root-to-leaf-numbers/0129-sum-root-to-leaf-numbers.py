# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        totalSum = 0
        def dfs(root, cur):
            nonlocal totalSum
            cur.append(str(root.val))
            if not root.left and not root.right:
                totalSum += int("".join(cur))
                return 
            if root.left:
                dfs(root.left, cur)
                cur.pop()
            if root.right:
                dfs(root.right, cur)
                cur.pop()
        dfs(root, [])
        return totalSum