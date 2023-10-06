# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        ans = []
        def dfs(root, cur_path, cur_sum):
            if not root:
                return 
            
            if not root.left and not root.right:
                if cur_sum + root.val == targetSum:
                    cur_path.append(root.val)
                    ans.append(cur_path.copy())
                return 
            
            dfs(root.left, cur_path + [root.val], cur_sum + root.val)
            dfs(root.right, cur_path + [root.val],  cur_sum + root.val)
            if cur_path:
                cur_path.pop()
            
            return 
        
        dfs(root, [], 0)
        
        return ans