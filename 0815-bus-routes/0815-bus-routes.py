class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        graph = defaultdict(list)
        que = deque([(source, 0)])
        visited = set()
        for i, route in enumerate(routes):
            for stop in route:
                graph[stop].append(i)
        
        while que:
            node, buses = que.popleft()
            visited.add(node)
            
            if node == target:
                return buses
            
            for idx in graph[node]:
                if routes[idx][0] == -1:
                    continue
                    
                for i, route in enumerate(routes[idx]):
                    routes[idx][i] = -1
                    
                    if route not in visited:
                        que.append((route, buses + 1))
            
        return -1 