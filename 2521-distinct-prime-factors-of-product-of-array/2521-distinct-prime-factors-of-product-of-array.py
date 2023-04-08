class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        prime_factors  = set()
        
        def factorization(num):
            divider = 2
            temp_factors = set()
            
            while divider * divider <= num:
                while num % divider == 0:
                    temp_factors.add(divider)
                    num //= divider
                divider += 1
                
            if num > 1:
                temp_factors.add(num)
            return temp_factors

        for num in nums:
            prime_factors = prime_factors | factorization(num)
        return len(prime_factors)