class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        degree = [0 for i in range(numCourses)]
        for course, pre_course in prerequisites:
            graph[pre_course].append(course)
        
            degree[course] += 1
        
        que = deque([])
        for i in range(numCourses):
            if degree[i] == 0:
                que.append(i)
        
        course_order = []
        
        while que:
            node = que.popleft()
            course_order.append(node)
            
            for child in graph[node]:
                degree[child] -= 1
                
                if degree[child] == 0:
                    que.append(child)
        
        return len(course_order) == numCourses