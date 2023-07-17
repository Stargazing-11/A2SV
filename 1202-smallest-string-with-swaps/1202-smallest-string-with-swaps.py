class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parents = list(range(len(s)))
        
        def find(node):
            root = node
            while root != parents[root]:
                root = parents[root]
            while node != parents[node]:
                temp = parents[node]
                parents[node] = root
                node = temp
            return root
            
        def union(node1, node2):
            p1, p2 = find(node1), find(node2)
            parents[p2] = p1

        for a, b in pairs:
            union(a, b)
            
        chars = defaultdict(list)
        indexs = defaultdict(list)
        
        for i, ch in enumerate(s):
            group = find(i)
            
            indexs[group].append(i)
            chars[group].append(ch)

        res = list(range(len(s)))
        
        for key in chars.keys():
            idx = sorted(indexs[key])
            chrs = sorted(chars[key])
            
            for i, c in zip(idx, chrs):
                res[i] = c
                
        return "".join(res)