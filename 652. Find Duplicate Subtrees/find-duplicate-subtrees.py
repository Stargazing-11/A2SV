# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        dupls = defaultdict(int)
        ans = []
        def dfs(root):
            
            if not root:
                return "-201"
            
            curr_path = str(root.val) + "," + dfs(root.left) + "," + dfs(root.right)
            if dupls[curr_path] == 1:
                ans.append(root)
            dupls[curr_path] += 1
            return curr_path
        
        dfs(root)
        
        return ans 