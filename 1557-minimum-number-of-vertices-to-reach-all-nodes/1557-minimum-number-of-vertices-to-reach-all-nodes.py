class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = {}
        for edge in edges:
            if edge[0] in graph:
                graph[edge[0]].append(edge[1])
            else:
                graph[edge[0]] = [edge[1]]
        
        output = []
        visited = set()
        
        def dfs(vertex):
            if vertex not in graph:
                return 
            for neighbor in graph[vertex]:
                visited.add(neighbor)
                if neighbor not in visited:
                    dfs(neighbor) 
        
        for key in graph.keys():
            dfs(key)
        for key in graph.keys():
            if key not in visited:
                output.append(key)
        return output