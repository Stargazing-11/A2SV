class Solution:
    def maxScore(self, nums: List[int]) -> int:
        max_score = [0]
        def calculateGcd(cur):
            gcds = []
            for a, b in cur:
                gcds.append(math.gcd(a,b))
            gcds.sort()
            cur_gcd = 0
            for i in range(n//2):
                cur_gcd += (i+1) * gcds[i]
            max_score[0] = max(max_score[0], cur_gcd)
        
        
        n = len(nums)
        
        def backtrack(cur, visited):
            if len(cur) == n // 2:
                calculateGcd(cur)
                return 
            
            start = -1
            for i, num in enumerate(nums):
                if i not in visited:
                    start = i 
                    break
                    
            for j in range(start+1, n):
                if j not in visited:
                    visited.add(j)
                    visited.add(start)
                    cur.append((nums[start], nums[j]))
                    backtrack(cur, visited)
                    if cur:
                        a, b = cur.pop()
                        visited.remove(j)
                        visited.remove(start)
            return 
        
        visited = set()
        backtrack([], visited)
        
        return max_score[0]
            
            
                