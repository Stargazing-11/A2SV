class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        z = Counter(words)
        y = sorted(sorted(z), key=z.get, reverse=True)
        c = 0
        out = []
        while(c < k):
            out.append(y[c])
            c += 1
        return out