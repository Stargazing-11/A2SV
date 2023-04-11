class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = {}
        
        for road in roads:
            if road[0] not in graph:
                graph[road[0]] = set()
                graph[road[0]].add(tuple(road))
            else:
                graph[road[0]].add(tuple(road))
            
            if road[1] not in graph:
                graph[road[1]] = set()
                graph[road[1]].add(tuple(road))
            else:
                graph[road[1]].add(tuple(road))
                
        keys = list(graph.keys())
        max_network = 0
        
        for i in range(len(keys)):
            for j in range(i + 1, len(keys)):
                temp = len(graph[keys[i]]) + len(graph[keys[j]])
                if (keys[i], keys[j]) in graph[keys[i]] or (keys[j], keys[i]) in graph[keys[i]]:
                    temp -= 1
                max_network = max(max_network, temp)
        
        return max_network