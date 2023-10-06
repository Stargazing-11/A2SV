class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = defaultdict(list)
        
        for value, (a, b) in zip(values, equations):
            graph[a].append((b, value))
            graph[b].append((a, 1 / value))
            
        
        def bfs(start, end):
            
            if start not in graph or end not in graph:
                return -1
            
            que = deque([(start, 1)])
            visited = set()
            
            while que:
                node, ans = que.popleft()
                
                if node == end:
                    return ans
                visited.add(node)
                for child, value in graph[node]:
                    if child not in visited:
                        que.append([child, ans * value])
            return -1
        
        res = []
        for a, b in queries:
            res.append(bfs(a, b))
            
        return res