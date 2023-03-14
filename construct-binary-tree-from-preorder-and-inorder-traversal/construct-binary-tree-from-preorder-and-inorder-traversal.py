# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        rootNode = TreeNode()
        def buildTree(root, turn, preorder, inorder):
            if preorder == []:
                return 
            
            new = TreeNode(preorder[0])
            if turn == 1:
                root.left = new
                root = root.left
            elif turn == 0:
                root.right = new
                root = root.right
                
            mid = inorder.index(preorder[0])    
            buildTree(root, 1, preorder[1:mid+1], inorder[:mid])
            buildTree(root, 0, preorder[mid+1:], inorder[mid+1:])
        
        buildTree(rootNode, 1, preorder, inorder)
        return rootNode.left