class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        
        ans = []
        cost = 0
        for num in instructions:
            left = len(ans) - bisect_right(ans, num)
            right = bisect_right(ans, num-1)
            
            cost += min(left, right)
            
            cost %= 10**9 + 7
            bisect.insort(ans, num)
        
        return cost