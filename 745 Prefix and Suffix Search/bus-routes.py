class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        routes = list(map(set, routes))
        graph = defaultdict(set)
        seen, targets = set(), set()
        
        if source == target:
            return 0
        for i, r1 in enumerate(routes):
            for j in range(i+1, len(routes)):
                r2 = routes[j]
                
                for r in r1:
                    if r in r2:
                        graph[i].add(j)
                        graph[j].add(i)
        
            if source in r1:
                seen.add(i)
            if target in r1:
                targets.add(i)
                
                
        queue = deque()

        for node in seen:
            queue.append((node, 1))

        while queue:
            node, depth = queue.popleft()

            if node in targets:
                return depth

            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append((neighbor, depth + 1))
        return -1
