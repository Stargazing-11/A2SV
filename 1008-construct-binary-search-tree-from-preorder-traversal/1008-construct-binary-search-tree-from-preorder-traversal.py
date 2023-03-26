# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        preorder = preorder
        root = TreeNode()
        
        def construct(root, start, end, turn):
            if start == end:
                return 
            left, right = start + 1, end-1
            
            while left <= right:
                mid = (left + right) // 2
                
                if preorder[mid] < preorder[start]:
                    left = mid + 1
                else:
                    right = mid - 1
            if turn == 0:
                root.left = TreeNode(preorder[start])
                construct(root.left, start+1, left,  0)
                construct(root.left, left, end,  1)
                
            else:
                root.right = TreeNode(preorder[start])

                construct(root.right, start+1, left,  0)
                construct(root.right, left, end,  1)
            
        construct(root, 0, len(preorder), 0)
        return root.left