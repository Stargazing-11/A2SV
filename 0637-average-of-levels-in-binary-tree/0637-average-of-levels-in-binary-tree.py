# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        averages = []

        def bfs(root):
            que = deque([(root, 0)])
            count = 0
            level = 0
            cur_sum = 0
            while que:
                node, lvl = que.popleft()
                if lvl != level:
                    level = lvl
                    averages.append(cur_sum / count)
                    cur_sum = 0
                    count = 0
                cur_sum += node.val
                count += 1
                if node.left:
                    que.append((node.left, level + 1))  
                if node.right:
                    que.append((node.right, level + 1))
            averages.append(cur_sum / count)
        bfs(root)
        return averages