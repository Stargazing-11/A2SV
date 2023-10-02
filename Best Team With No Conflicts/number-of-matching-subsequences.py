class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = 0
    
class Solution:
    
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            
            cur = cur.children[c]
        
        cur.isEnd += 1
    
    def search(self, s, count):
        cur = self.root
        count = [0]

        def dfs(node, idx):
            count[0] += node.isEnd

            if not node.children:
                return 

            for child in node.children:
                for i in range(idx, len(s)):
                    if s[i] == child:
                        dfs(node.children[child], i+1)
                        break
            return 
        dfs(cur, 0)
        return count[0]
        
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:

        for word in words:
            self.insert(word)

        return self.search(s, 0)
        
