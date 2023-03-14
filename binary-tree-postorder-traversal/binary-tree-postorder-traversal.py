# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stk = [[root, True]]
        
        cur = root
        
        while cur or stk:
            while cur:
                stk.append([cur.right, False])
                cur = cur.left
                stk.append([cur, True])
            temp = stk.pop()
            if temp[-1] == True and temp[0] != None:
                ans.append(temp[0].val)
            elif temp[-1] == False:
                temp[-1] = True
                stk.append(temp)
                cur = temp[0]
        return ans