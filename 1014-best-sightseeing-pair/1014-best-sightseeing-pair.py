class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
        ans = float('-inf')
        cur_value = values[0]
        
        
        for j in range(1, len(values)):
            ans = max(ans, cur_value + values[j] - j)
            cur_value = max(cur_value, values[j] + j)
        return ans