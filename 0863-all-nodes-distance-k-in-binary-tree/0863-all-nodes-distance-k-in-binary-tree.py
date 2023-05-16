# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        graph = defaultdict(list)
        
        def traverse(root):
            
            if root.left:
                graph[root.val].append(root.left.val)
                graph[root.left.val].append(root.val)
                traverse(root.left)
            if root.right:
                graph[root.val].append(root.right.val)
                graph[root.right.val].append(root.val)
                traverse(root.right)
        traverse(root)
        
        que = deque([])
        que.append((target.val, 0))
        
        visited = {target.val}
        ans = []

        while que:
            node, length = que.popleft()
            if length == k:
                ans.append(node)
                
            for child in graph[node]:
                if child not in visited:
                    que.append((child, length+1))
                    visited.add(child)
        return ans
                
                