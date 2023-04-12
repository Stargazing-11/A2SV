class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        
        for vert, hate in dislikes:
            graph[vert].append(hate)
            graph[hate].append(vert)
            
        colors = [0 for i in range(n)]
        
        def dfs(vertex, color):
            if colors[vertex-1] != 0:
                if colors[vertex-1] != color:
                    return False
                return True
            
            colors[vertex-1] = color
            
            for neighbor in graph[vertex]:
                ans = dfs(neighbor, -(color))
                if ans == False:
                    return False
            return True

        for i in range(1, n+1):
            if colors[i-1] == 0:
                ans = dfs(i, -1)
                if ans == False:
                    return False
        return True
            
            