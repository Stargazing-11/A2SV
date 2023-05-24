class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        letters = defaultdict(int)
        numbers = defaultdict(int)
        range1, range2 = range(0, 26), range(97, 97 + 26)
        parents = [] 

        for i, j in zip(range1, range2):
            letters[chr(j)] = i
            numbers[i] = chr(j)
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

        for equation in equations:
            letter1 = letters[equation[0]]
            letter2 = letters[equation[3]]
            
            sign = equation[1]
            
            if sign == "=":
                union(letter1, letter2)
        
        for equation in equations:
            letter1 = letters[equation[0]]
            letter2 = letters[equation[3]]
            
            if equation[1] == "!" and find(letter1) == find(letter2):
                return False
        return True