class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
       
        graph = defaultdict(list)
        for a, b, t in meetings:
            graph[t].append([a,b])

        parents = [i for i in range(n)]
        secrets = [False for i in range(n)]
        
        def union(node1, node2):
            p1, p2 = find(node1), find(node2)
            
            if p1 > p2:
                p1, p2 = p2, p1
            
            parents[p2] = p1
        
        def find(node):
            root = node
            
            while root != parents[root]:
                root = parents[root]
                
            while node != parents[node]:
                temp = parents[node]
                parents[node] = root
                node = temp
            return root
        
        union(0, firstPerson)
        
        secrets[0] = True
        secrets[firstPerson] = True

        keys = sorted(graph.keys())
        
        for key in keys:
            for a, b in graph[key]:            
                union(a,b)
            
            for a, b in graph[key]:
                if find(a) != 0:
                    parents[a] = a
                    parents[b] = b
                else:
                    secrets[a] = True
                    secrets[b] = True
        
        ans = [i for i in range(n) if secrets[i]]
        return ans 
            