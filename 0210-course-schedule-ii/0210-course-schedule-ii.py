class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
       
        graph = defaultdict(list)
        degree = [0 for i in range(numCourses)]
        for course, pre_course in prerequisites:
            graph[pre_course].append(course)

        course_order = []
        def dfs(root):
            degree[root] = 1
            for child in graph[root]:
                if degree[child] == 1:
                    return 
                elif degree[child] == 0:
                    dfs(child)
            course_order.append(root)
            degree[root] = 2
            return 
        keys = list(graph.keys())
        
        for key in range(numCourses):
            if degree[key] == 0:
                dfs(key)
        course_order.reverse()
        return course_order if len(course_order) == numCourses else []
