class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        
        
        for start, end, time in times:
            graph[start].append((time, end))
            
        def dijkstra(start):
            distances = {node: float('inf') for node in range(1, n+1)}
            
            distances[start] = 0
            visited = set()

            heap = [(0, start)]

            while heap:
                cur_distance, node = heapq.heappop(heap)

                if node in visited:
                    continue
                visited.add(node)
                
                for weight, child in graph[node]:
                    distance = cur_distance + weight
                    if distance < distances[child]:
                        distances[child] = distance
                        
                        heapq.heappush(heap, (distance, child))
            
            return distances
        ans = max(dijkstra(k).values())
        
        if ans == float('inf'):
            return - 1
        return ans