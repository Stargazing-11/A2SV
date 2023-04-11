class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = {}
        degrees = {}
        new_roads = set()
        for city1, city2 in roads:
            new_roads.add((city1, city2))
            
            degrees[city1] = degrees.get(city1, 0) + 1
            degrees[city2] = degrees.get(city2, 0) + 1
            
        keys = list(degrees.keys())
        max_network = 0
        
        for i in range(len(keys)):
            for j in range(i + 1, len(keys)):
                temp = degrees[keys[i]] + degrees[keys[j]]
                if (keys[i], keys[j]) in new_roads or (keys[j], keys[i]) in new_roads:
                    temp -= 1
                max_network = max(max_network, temp)
        return max_network
