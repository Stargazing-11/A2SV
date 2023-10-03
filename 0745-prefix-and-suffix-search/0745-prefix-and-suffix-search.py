class TrieNode:
    def __init__(self):
        self.children = {}
        self.index = -1

class WordFilter:

    def __init__(self, words: List[str]):
        self.root = TrieNode()
        
        for i, word in enumerate(words):
            for j in range(len(word)):
                new = word[j:] + "#" + word
                self.insert(new, i)

    def f(self, pref: str, suff: str) -> int:
        prefx = suff + "#" + pref
        
        return self.startWith(prefx)
        
    def insert(self, word, i):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            
            cur = cur.children[c]
            cur.index = max(cur.index, i)
    
    def startWith(self, pref):
        cur = self.root
        for c in pref:
            if c not in cur.children:
                return -1
            
            cur = cur.children[c]
        
        return cur.index     
    
# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)