class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        graph = defaultdict(list)
        
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
            
        visited = {0}
        
        ans = [0]
        
        def dfs(root):
            temp = 0
            for child in graph[root]:
                if child not in visited:
                    visited.add(child)
                    res = dfs(child)
                    if res:
                        ans[0] += 2
                        temp = 1
            return 1 if temp or hasApple[root] else 0
        dfs(0)
        return ans[0]