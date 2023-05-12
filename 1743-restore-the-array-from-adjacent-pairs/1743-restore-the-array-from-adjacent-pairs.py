class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        indegree = defaultdict(int)
        graph = defaultdict(list)
        
        for a, b in adjacentPairs:
            graph[a].append(b)            
            graph[b].append(a)

            indegree[a] += 1
            indegree[b] += 1

        first_child = None
        for key in indegree.keys():
            if indegree[key] == 1:
                first_child = key
                break
        visited = set()
        ans = []
        def dfs(node):
            ans.append(node)
            visited.add(node)
            
            for child in graph[node]:
                if child not in visited:
                    dfs(child)
        dfs(first_child)
        return ans
        