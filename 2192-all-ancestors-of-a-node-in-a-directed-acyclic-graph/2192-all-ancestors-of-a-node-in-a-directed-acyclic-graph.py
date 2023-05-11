class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        indegree = [0 for i in range(n)]
        graph = defaultdict(list)
        
        for i in range(len(edges)):
            frm, to = edges[i]
            graph[frm].append(to)
            indegree[to] += 1
            
        que = deque([])
        ans = [set() for i in range(n)]
        for i in range(len(indegree)):
            
            if indegree[i] == 0:
                que.append(i)
                
        def bfs():
            
            while que:
                node = que.popleft()
                
                for child in graph[node]:
                    ans[child].update(ans[node])
                    ans[child].add(node)

                    indegree[child] -= 1
                    if indegree[child] == 0:
                        que.append(child)
        bfs()
        return [sorted(ans[i]) for i in range(len(ans))]