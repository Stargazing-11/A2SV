class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = 0

class MapSum:

    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, key: str, val: int) -> None:
        cur = self.root
        
        for c in key:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = val

    def sum(self, prefix: str) -> int:
        cur = self.root
        total = [0]
        
        def dfs(node):
            total[0] += node.end
            if not node.children:
                return 
            
            for child in node.children:
                dfs(node.children[child])
            return 
        
        for c in prefix:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return 0
        dfs(cur)
        return total[0]
        

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)