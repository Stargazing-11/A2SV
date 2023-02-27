class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        arr = [[0 for i in range(n)] for i in range(n)]
        pref_sum = [[0 for i in range(n+1)] for i in range(n+1)]
        
        for query in queries:
            arr[query[0]][query[1]] += 1
            
            if query[3] + 1 < n:
                arr[query[0]][query[3] + 1] -= 1
            if query[2] + 1 < n:
                arr[query[2]+1][query[1]] -= 1
            if query[2] + 1 < n and query[3] + 1 < n:
                arr[query[2]+1][query[3]+1] += 1

        for i in range(1, len(pref_sum)):
            for j in range(1, len(pref_sum)):
                pref_sum[i][j] = pref_sum[i-1][j] + pref_sum[i][j-1] + arr[i-1][j-1] - pref_sum[i-1][j-1]
        slice = [pref_sum[i][1:] for i in range(1,n+1)]
        return slice