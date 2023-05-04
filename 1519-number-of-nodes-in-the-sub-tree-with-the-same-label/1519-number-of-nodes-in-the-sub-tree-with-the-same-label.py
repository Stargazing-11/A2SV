class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        def getDict():
            d = {}
            for asc in range(ord('a'), ord('z')+1):
                d[chr(asc)] = 0
            return d
        
        ans = [1 for i in range(n)]
        visited = {0}
        
        def dfs(node):
            current_dict = getDict()
            current_dict[labels[node]] += 1
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    neighbor_dict = dfs(neighbor)
                    for ch in current_dict:
                        current_dict[ch] += neighbor_dict[ch]
            ans[node] = current_dict[labels[node]]
            return current_dict
        
        dfs(0)
        
        return ans
            