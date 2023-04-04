# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        traverse_dict = defaultdict(list)
        def traverse(root, col, row):
            if not root:
                return 
            
            traverse_dict[row].append(col)
            
            traverse(root.left, (2 *col) -1, row+1)
            traverse(root.right, col *2, row+1)
            
        traverse(root, 1, 0)
        
        width = 1
        for key in sorted(traverse_dict.keys()):
            if len(traverse_dict[key]) == 1:
                continue
            width = max(width, (traverse_dict[key][-1] - traverse_dict[key][0] + 1))
        return width
            
            