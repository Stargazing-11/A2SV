class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        
        def find_gcd(num1, num2):
            if num2 == 0:
                return num1
            
            return find_gcd(num2, num1 % num2)
        
        
        count = 0
        
        for index in range(len(nums)):
            gcd = nums[index]
            for ind in range(index, len(nums)):
                
                gcd = find_gcd(gcd, nums[ind])
                
                if gcd == k:
                    count += 1
        return count 