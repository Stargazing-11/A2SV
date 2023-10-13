class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)            
            graph[b].append(a)
            
        freq = [0 for i in range(n)]
        def bfs(start, end):
            que = deque([(start, [start])])
            visited = set()
            
            while que:
                node, path = que.pop()
                visited.add(node)
                
                if node == end:
                    return path
                
                for child in graph[node]:
                    if child not in visited:
                        que.append((child, path + [child]))
                                   
        for start, end in trips:
            path = bfs(start, end)
            
            for node in path:
                freq[node] += 1
                                   
        cache = {}
        def dp(node,parent, state):
            
            if (node, parent, state) in cache:
                return cache[(node, parent, state)]
            
            if state:
                cur_cost = (freq[node] * price[node]  // 2)
            else:
                cur_cost = freq[node] * price[node]
                
            for child in graph[node]:
                if child != parent:
                    if state:
                        child_cost = dp(child, node, not state)
                    else:
                        child_cost = min(dp(child, node, not state), dp(child, node, state))
                    cur_cost += child_cost
                    
            cache[(node, parent, state)] = cur_cost
            return cur_cost

        min_cost = float('inf')
        for node in range(n):
            min_cost = min(min_cost, dp(node, None, True), dp(node, None, False))
        return min_cost
        
        

