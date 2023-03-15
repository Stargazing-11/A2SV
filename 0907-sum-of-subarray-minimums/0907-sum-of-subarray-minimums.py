class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        prevMin = [-1 for _ in range(len(arr))]
        monStk = []
        mod = pow(10, 9) + 7
        
        for i in range(len(arr)):
            while monStk and arr[monStk[-1]] > arr[i]:
                monStk.pop()
                
            if monStk:
                prevMin[i] = monStk[-1]
            monStk.append(i)
            
        result = [0 for i in range(len(arr))]
        
        for i in range(len(arr)):
            val = result[prevMin[i]] if prevMin[i] != -1 else 0
            result[i] = val + (i - prevMin[i]) * arr[i]
        return sum(result) % mod