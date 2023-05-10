class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        indegree = defaultdict(list)
        graph = defaultdict(list)
        for i in range(len(recipes)):
            indegree[recipes[i]] = 0
            
        for i in range(len(recipes)):
            for j in range(len(ingredients[i])):
                
                graph[ingredients[i][j]].append(recipes[i])
                indegree[recipes[i]] += 1
        
        
        que = deque([])
        for sup in supplies:
            que.append(sup)
        ans = []
        while que:
            ingredient = que.popleft()
            
            for child in graph[ingredient]:
                indegree[child] -= 1
                
                if indegree[child] == 0:
                    ans.append(child)
                    que.append(child)
        return ans 