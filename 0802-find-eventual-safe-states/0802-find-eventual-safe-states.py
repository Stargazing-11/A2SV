class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        connected = defaultdict(list)
        indegree = [0 for i in range(len(graph))]

        ans = []    
        def dfs(node):
            if indegree[node] != 0:
                if indegree[node] == 1:
                    return False
                return True
            
            indegree[node] = 1
            for child in graph[node]:
                if indegree[child] == 1:
                    return False
                elif not dfs(child):
                    return False
            indegree[node] = 2
            return True
        
        for i in range(len(graph)):
            if dfs(i):
                ans.append(i)
        return sorted(ans)
