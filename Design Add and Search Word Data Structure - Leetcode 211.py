class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        n = len(word)
        def dfs(i, root):
            cur = root

            for j in range(i, n):
                c = word[j]

                if c == ".":
                    for child in cur.children.values():
                        if dfs(j+1, child):
                            return True
                    return False
                
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.isEnd
        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
