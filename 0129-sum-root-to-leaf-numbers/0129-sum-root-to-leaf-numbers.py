# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        totalSum = 0
        def dfs(root, cur_sum):
            nonlocal totalSum
            cur_sum = cur_sum * 10 + root.val
            if not root.left and not root.right:
                totalSum += cur_sum
                return 
            if root.left:
                dfs(root.left, cur_sum)
            if root.right:
                dfs(root.right, cur_sum)
                cur_sum -= root.val
        dfs(root, 0)
        return totalSum