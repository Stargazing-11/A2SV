# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_store = defaultdict(list)
        
        stk = []
        cur = root
        level = 0
        while stk or cur:
            while cur:
                stk.append((cur, level))
                cur = cur.left
                level += 1
            node, lvl = stk.pop()
            level_store[lvl].append(node.val)
            
            if node.right:
                level = lvl + 1
                cur = node.right
        return [level_store[key] for key in sorted(level_store.keys())]