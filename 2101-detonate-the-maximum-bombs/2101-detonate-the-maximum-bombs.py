class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = {}
        
        for i in range(len(bombs)):
            for j in range(i+1, len(bombs)):   
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]
                distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
                
                if distance <= r1:
                    graph.setdefault(i, []).append(j)
                if distance <= r2:
                    graph.setdefault(j, []).append(i)

        visited, max_det = set(), [1]
        count = [1]
        def dfs(vertex):
            visited.add(vertex)
            if vertex not in graph:
                return 
            
            for child in graph[vertex]:
                if child not in visited:
                    count[0] += 1
                    dfs(child)
                    
        for key in graph.keys():
            visited, count = set(), [1]
            dfs(key)
            max_det = [max(max_det[0], count[0])]
        return max_det[0]