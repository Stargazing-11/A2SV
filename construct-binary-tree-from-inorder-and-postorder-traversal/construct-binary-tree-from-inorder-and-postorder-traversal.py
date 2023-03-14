# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        rootNode = TreeNode()
        def buildTree(root, turn, postorder, inorder):
            if postorder == []:
                return 
            
            new = TreeNode(postorder[-1])
            if turn == 1:
                root.left = new
                root = root.left
            elif turn == 0:
                root.right = new
                root = root.right
                
            mid = inorder.index(postorder[-1])    
            buildTree(root, 1, postorder[:mid], inorder[:mid])
            buildTree(root, 0, postorder[mid:-1], inorder[mid+1:])
        
        buildTree(rootNode, 1, postorder, inorder)
        return rootNode.left