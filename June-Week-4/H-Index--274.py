class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        citations.sort()
        citations.reverse()
        N = len(citations)
        for i, j in enumerate(citations):
            if i >= j:
                return i
        return N
                