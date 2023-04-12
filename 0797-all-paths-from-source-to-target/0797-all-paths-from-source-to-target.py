class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        paths = {}
        
        for i in range(len(graph)):
            paths[i] = [graph[i]]

        output = []
        def dfs(cur, vertex):
            if cur[-1] == len(graph)-1:
                output.append(cur.copy())
                return 

            for neighbor in graph[vertex]:
                cur.append(neighbor)
                dfs(cur, neighbor)
                cur.pop()
        dfs([0], 0)
        return output