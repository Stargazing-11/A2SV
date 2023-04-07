class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph = defaultdict(list)
        
        for edg in edges:
            graph[edg[0]].append(edg[1])
            graph[edg[1]].append(edg[0])
        
        visited = set()
        
        def dfs(vertex, visited):
            if vertex == destination:
                return True
            
            visited.add(vertex)
            
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    ans = dfs(neighbor, visited)
                    if ans:
                        return True
            return False
        
        return dfs(source, visited)