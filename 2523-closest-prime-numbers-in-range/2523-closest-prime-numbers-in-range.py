class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def prime_sieve(n: int) -> list[bool]:
            is_prime: list[bool] = [True for _ in range(n + 1)]
            is_prime[0] = is_prime[1] = False

            i = 2

            while i * i <= n:
                if is_prime[i]:
                    j = i * i
                    while j <= n:
                        is_prime[j] = False
                        j += i
                i += 1

            return [i for i in range(left, right+1) if is_prime[i]==True]
        primes = prime_sieve(right)
        
        if len(primes) < 2:
            return [-1, -1]
        ans, min_gap = [primes[0], primes[1]], primes[1] - primes[0]
        
        for i in range(2, len(primes)):
            if primes[i] - primes[i-1] < min_gap:
                ans = [primes[i-1], primes[i]]
                min_gap = primes[i] - primes[i-1]
                
        return ans