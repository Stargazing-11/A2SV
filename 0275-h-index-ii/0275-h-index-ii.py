class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        N = len(citations)
        left, right = 0, len(citations) - 1
        ans = []
        
        while left <= right:
            mid = (left + right)//2
            
            if N - mid <= citations[mid]:
                right = mid - 1
                ans.append(N-mid)
            elif N - mid > citations[mid]:
                left = mid + 1
        return ans[-1] if ans else 0