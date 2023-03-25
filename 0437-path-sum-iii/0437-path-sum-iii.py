# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = 0
        prefix_freq = {0:1}
        paths = []
        prefix = 0
        def path(root, cur):
            nonlocal prefix
            nonlocal count
            if not root:
                return 
            # print(prefix_freq, cur, prefix, count)
            cur.append(root.val)
            prefix += root.val
            if prefix - targetSum in prefix_freq:
                count += prefix_freq[prefix - targetSum]
            prefix_freq[prefix] = prefix_freq.get(prefix,0) + 1
            
            # print(prefix_freq, cur, prefix, count)
            
            if not root.left and not root.right:
                return 
            if root.left:
                path(root.left, cur)
                prefix_freq[prefix] -= 1
                prefix -= cur.pop()
            if root.right:
                path(root.right, cur)
                prefix_freq[prefix] -= 1
                prefix -= cur.pop()
            return 
        path(root, [])
        return count