class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parents = {}
        
        def find(node):
            root = node
            while root != parents[root]:
                root = parents[root]
            
            while node != parents[node]:
                temp = parents[node]
                parents[node] = root
                node = temp
            return root
        
        def union(node1, node2):
            if node1 not in parents:
                parents[node1] = node1
            
            if node2 not in parents:
                parents[node2] = node2
            
            p1, p2 = find(node1), find(node2)
            parents[p2] = p1
            
        
        for node1, node2 in stones:
            union(node1, -node2-1)
        
        roots = set()
        
        for key in parents:
            root = find(key)
            roots.add(root)
            
        return len(stones) - len(roots)
        
        