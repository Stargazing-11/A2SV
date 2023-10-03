class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = 0

class Solution:
    
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        curr = self.root
        
        for c in word:
            # print(c, word, curr.children, curr.isEnd)
            if c not in curr.children:
                curr.children[c] = TrieNode()
            # curr.children[c].isEnd += 1
            curr = curr.children[c]
            curr.isEnd += 1
            # curr.isEnd += 1
    
    def search(self, word):
        curr = self.root
        count = [0]
        
        for c in word:
            if c not in curr.children:
                return count[0]
            curr = curr.children[c]
            count[0] += curr.isEnd
        return count[0]
        
        
#         def dfs(node):
            
#             count[0] += node.isEnd
            
#             if not node.children:
#                 return 
            
#             for child in curr.children:
#                 dfs(curr.children[child])
#             return 
        
#         for c in word:
#             if c not in curr.children:
#                 return 0
            
#             curr = curr.children[c]
#         dfs(curr)
        # return count[0]
    
    def printTrie(self, new):
        if not new.children:
            return 
        print(new.children, new.isEnd, "top")
        for idx, child in enumerate(new.children):
            if child:
                print(child)
                if child not in new.children:
                    return 
                new = new.children[child]
                print(new.children, "bottom")
                self.printTrie(new)
    
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        
        for word in words:
            self.insert(word)
        ans = []
        
        for word in words:
            ans.append(self.search(word))
        
        return ans 
        
        
        