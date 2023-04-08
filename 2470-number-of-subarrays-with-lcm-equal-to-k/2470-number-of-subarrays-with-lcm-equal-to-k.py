class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        
        def find_lcm(a, b):
            return abs(a*b) // math.gcd(a, b)
        
        count = 0
        for i in range(len(nums)):
            lcm = nums[i]
            
            for j in range(i, len(nums)):
                
                lcm = find_lcm(lcm, nums[j])
                
                if lcm == k:
                    count += 1
        return count