class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        graph = defaultdict(list)
        
        for succ, (a, b) in zip(succProb, edges):
            graph[a].append((b, succ))
            graph[b].append((a, succ))
            
        visited = set()
        heap = [(-1, start_node)]
        heapq.heapify(heap)
        
        while heap:
            rate, node = heapq.heappop(heap)
            if node == end_node:
                return rate * (-1)
            visited.add(node)
            
            for child, weight in graph[node]:
                if child not in visited:
                    new_rate = weight * rate
                    heapq.heappush(heap, (new_rate, child))
        return 0
                    
                    
                    