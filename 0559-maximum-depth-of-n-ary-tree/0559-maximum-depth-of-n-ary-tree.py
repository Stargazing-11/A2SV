"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        max_depth = 0
        def dfs(root, depth):
            nonlocal max_depth
            if not root:
                return 
            max_depth = max(max_depth, depth)
            for child in root.children:
                dfs(child, depth+1)
        dfs(root, 1)
        
        return max_depth