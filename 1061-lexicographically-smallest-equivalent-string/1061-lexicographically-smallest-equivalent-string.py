class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        letters = defaultdict(int)
        numbers = defaultdict(int)
        range1, range2 = range(0, 26), range(97, 97 + 26)
        rank = []
        parents = [] 
        
        for i, j in zip(range1, range2):
            letters[chr(j)] = i
            numbers[i] = chr(j)
            rank.append(i)
            parents.append(i)
            
        def find(node):
            root = node
            
            while parents[root] != root:
                root = parents[root]
            
            while node != parents[node]:
                temp = parents[node]
                parents[node] = root
                node = temp
                
            return root
        
        def union(node1, node2):
            p1, p2 = find(node1), find(node2)

            if p1 > p2:
                p1, p2 = p2, p1
                
            parents[p2] = p1
            
        for letter1, letter2 in zip(s1, s2):
            letter1 = letters[letter1]
            letter2 = letters[letter2]
            
            union(letter1, letter2)
        ans = []

        for letter in baseStr:
            parent = find(letters[letter])
            ans.append(numbers[parent])
        
        return "".join(ans)