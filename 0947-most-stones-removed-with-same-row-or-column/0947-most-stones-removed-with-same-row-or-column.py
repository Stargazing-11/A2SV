class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        row_len = float('-inf')
        col_len = float('-inf')
        for i, j in stones:
            row_len = max(row_len, i)
            col_len = max(col_len, j)

        parents = {}
            
        for i, j in stones:
            parents[i] = i
            parents[j + row_len + 1] = j + row_len + 1 
        
        
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
            p1, p2 = find(node1), find(node2)
            parents[p2] = p1
            
        
        for i, j in stones:
            union(i, j + row_len + 1)
        
        roots = set()
        
        for key in parents:
            root = find(key)
            roots.add(root)
            
        return len(stones) - len(roots)
        
        