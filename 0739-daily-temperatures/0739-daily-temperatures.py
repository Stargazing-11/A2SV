class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0 for i in range(len(temperatures))]
        monStk = []
        
        for index, temp in enumerate(temperatures):
            while monStk and temperatures[monStk[-1]] < temp:
                ind = monStk.pop()
                ans[ind] = index - ind
                
            monStk.append(index)
        return ans