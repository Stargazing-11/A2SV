# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        ans = defaultdict(int)
        
        def modes(root):
            if not root:
                return
                
            ans[root.val] += 1
            
            modes(root.left)
            modes(root.right)
            
        modes(root)
        output = []

        for key in ans.keys():
            while output and ans[key] > ans[output[-1]]:
                output.pop()
            if not output or ans[output[-1]] == ans[key]:
                output.append(key)
        return output