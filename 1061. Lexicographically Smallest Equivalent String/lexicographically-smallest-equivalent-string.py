class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        parents = [i for i in range(26)]
        
        letters = {chr(i + 97): i for i in range(26)}        
        numbers = {i: chr(i + 97) for i in range(26)}
        def union(node1, node2):
            p1, p2 = find(node1), find(node2)
            if p1 > p2:
                p1, p2 = p2, p1
            parents[p2] = p1
        
        def find(node):
            root = node
            while parents[root] != root:
                root = parents[root]
            
            while node != parents[node]:
                temp = parents[node]
                parents[node] = root
                node = temp
            return root
        
        for l1, l2 in zip(s1, s2):
            union(letters[l1], letters[l2])

        ans = []
        for l in baseStr:
            n = letters[l]
            ans.append(numbers[find(n)])
        return "".join(ans)
            
            
            
            