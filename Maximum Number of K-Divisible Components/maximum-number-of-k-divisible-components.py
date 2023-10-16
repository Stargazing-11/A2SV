class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        
        graph = defaultdict(list)
        for a, b in edges:
            graph[b].append(a)
            graph[a].append(b)
         
        count = [0]
        visited = set()
        def dfs(node):
            visited.add(node)
            ans = 0
            for child in graph[node]:
                if child not in visited:
                    ans += dfs(child)
                    
            ans += values[node]
            if ans % k:
                return ans
            count[0] += 1
            return 0
        
        dfs(0)
        
        return count[0]