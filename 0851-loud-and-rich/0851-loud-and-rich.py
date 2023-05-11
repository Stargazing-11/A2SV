class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        indegree = [0 for i in range(len(quiet))]
        graph = defaultdict(list)
        
        for a, b in richer:
            graph[a].append(b)
            indegree[b] += 1
        que = deque([])
        ans = [i for i in range(len(quiet))]
        
        for i in range(len(quiet)):
            if indegree[i] == 0:
                que.append(i)
        
        def findQuiet(cur_min, cur_node, node, child):
            indices = [cur_min, cur_node, node, child]
            min_index = None

            for index in indices:
                if index < len(quiet):
                    if min_index is None or quiet[index] < quiet[min_index]:
                        min_index = index
            return min_index
        
        def bfs():
            while que:
                node = que.popleft()
                
                for child in graph[node]:
                    cur = findQuiet(ans[child], ans[node], node, child)
                    ans[child] = cur 
                    indegree[child] -= 1
                    if indegree[child] == 0:
                        que.append(child)

        bfs()
        return ans 