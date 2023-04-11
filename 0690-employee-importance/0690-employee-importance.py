"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = {}
        
        for emp in employees:
            graph[emp.id] = [emp.importance, emp.subordinates]
        
        
        output = 0
        def dfs(employee):
            nonlocal output
            output += graph[employee][0]
            for subord in graph[employee][1]:
                dfs(subord)
        dfs(id)
        return output