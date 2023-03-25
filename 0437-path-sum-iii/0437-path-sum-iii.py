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
        
        def calculatePrefix(value):
            nonlocal prefix
            nonlocal count
            prefix += value
            if prefix - targetSum in prefix_freq:
                count += prefix_freq[prefix - targetSum]
            prefix_freq[prefix] = prefix_freq.get(prefix,0) + 1
            
        def removePrefix(value, num):
            nonlocal prefix
            prefix_freq[prefix] -= 1
            prefix -= num
            
            
        def path(root, cur):
            if not root:
                return 
            cur.append(root.val)
            calculatePrefix(root.val)
           
            if not root.left and not root.right:
                return 
            
            if root.left:
                path(root.left, cur)
                removePrefix(prefix, cur.pop())
            if root.right:
                path(root.right, cur)
                removePrefix(prefix, cur.pop())
            
        path(root, [])
        return count