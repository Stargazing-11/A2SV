# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode()
        
        def binarySearch(left, right, target):
            while left <= right:
                mid = (left + right) // 2
                if preorder[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        
        def construct(root, start, end, turn):
            if start == end:
                return 
            left = binarySearch(start+1, end-1, preorder[start])
            
            if turn == 0:
                root.left = TreeNode(preorder[start])
                newRoot = root.left
            else:
                root.right = TreeNode(preorder[start])
                newRoot = root.right
                
            construct(newRoot, start+1, left,  0)
            construct(newRoot, left, end,  1)
            
        construct(root, 0, len(preorder), 0)
        return root.left