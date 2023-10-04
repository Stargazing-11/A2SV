class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        prereqs = defaultdict(set)
        indegree = [0 for i in range(numCourses)]
        
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
            
        que = deque([i for i in range(numCourses) if indegree[i] == 0])
        
        while que:
            node = que.popleft()
            for child in graph[node]:
                indegree[child] -= 1
                
                for pre in prereqs[node]:
                    prereqs[child].add(pre)
                
                prereqs[child].add(node)
                if indegree[child] == 0:
                    que.append(child)

        ans = []        
        for a, b in queries:
            if b in prereqs[a]:
                ans.append(True)
            else:
                ans.append(False)
                
        return ans