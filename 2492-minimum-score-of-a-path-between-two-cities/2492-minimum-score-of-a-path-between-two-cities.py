class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        min_score = float("inf")
        
        graph = defaultdict(list)
        
        for a, b, distance in roads:
            graph[a].append((b, distance))
            graph[b].append((a, distance))
        
        
        que = deque([])
        que.append(1)
        
        visited = set()
        
        while que:
            node = que.popleft()
            visited.add(node)
            
            for child, distance in graph[node]:
                if child not in visited:
                    min_score = min(min_score, distance)
                    que.append(child)
        return min_score