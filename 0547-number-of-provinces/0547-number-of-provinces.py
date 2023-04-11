class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = {}
        visited = set()
        provinces = 0

        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1:
                    if i not in graph:
                        graph[i] = []
                    graph[i].append(j)
       
        def dfs(vertex):
            nonlocal provinces
            visited.add(vertex)
            
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    dfs(neighbor)
                    
        for key in graph.keys():
            if key not in visited:
                dfs(key)
                provinces += 1
        
        return provinces