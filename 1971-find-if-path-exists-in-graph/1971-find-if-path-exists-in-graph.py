class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        parents = list(range(n))
        rank = [1 for i in range(n)]
        
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
            parent1 = find(node1)
            parent2 = find(node2)
            
            if rank[node1] < rank[node2]:
                parent1, parent2 = parent2, parent1
                
            parents[parent2] = parent1
            rank[parent1] += rank[parent2]
            
            return False
        
        for node1, node2 in edges:
            union(node1, node2)
            
        return find(source) == find(destination)
