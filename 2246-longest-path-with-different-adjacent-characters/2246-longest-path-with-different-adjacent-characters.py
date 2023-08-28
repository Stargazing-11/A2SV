class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        
        graph = defaultdict(list)
        
        for i, p in enumerate(parent):
            graph[p].append(i)
            
        ans = [1]
        
        def dfs(node):
            
            longest, second_longest = 0, 0
            
            for child in graph[node]:
                cur_path_length = dfs(child)
                
                if s[node] != s[child]:
                    
                    if cur_path_length > longest:
                        second_longest = longest
                        longest = cur_path_length
                        
                    elif cur_path_length > second_longest:
                        second_longest = cur_path_length
                    
            ans[0] = max(ans[0], longest + second_longest + 1)
            
            return longest + 1
        
        dfs(0)
        return ans[0]