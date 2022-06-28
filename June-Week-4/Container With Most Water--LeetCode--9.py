class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        mon_stk = []
        first, second = 0, len(height) - 1
        total = 0
        while(first != second):
            temp = min(height[first], height[second]) * (second-first)
            total = max(total, temp)
            
            if height[first] > height[second]:
                second -=1
            else:
                first +=1
        return total