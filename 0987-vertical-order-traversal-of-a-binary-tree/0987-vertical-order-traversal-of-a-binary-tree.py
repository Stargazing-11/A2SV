# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        vertical_order = defaultdict(list)
        
        def traverse(root, row_col):
            if not root:
                return 
            
            vertical_order[row_col[1]].append((row_col[0], root.val))
            
            traverse(root.left, (row_col[0] + 1, row_col[1] - 1))
            traverse(root.right, (row_col[0] + 1, row_col[1] + 1))
            
        traverse(root, (0, 0))
        ans = []
        for key in sorted(vertical_order.keys()):
            temp = []
            for val in sorted(vertical_order[key]):
                temp.append(val[1])
            ans.append(temp)
        return ans
            