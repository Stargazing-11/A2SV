class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        word_frq = [Counter(word)[sorted(word)[0]] for word in words]
        query_frq = [Counter(query)[sorted(query)[0]] for query in queries]
        
        word_frq.sort()
        
        ans = [0 for i in range(len(queries))]
        
        for i, query in enumerate(query_frq):
            left, right = 0, len(word_frq) - 1
            
            while left <= right:
                mid = (left + right) // 2
                
                if word_frq[mid] <= query:
                    left = mid + 1
                elif word_frq[mid] > query:
                    right = mid - 1
            ans[i] = (len(word_frq) - left)
        return (ans)