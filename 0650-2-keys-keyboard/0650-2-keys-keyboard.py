class Solution:
    def minSteps(self, n: int) -> int:
        def prime_sieve(n):
            is_prime = [True for _ in range(n + 1)]
            is_prime[0] = is_prime[1] = False

            i = 2
            while i * i <= n:
                if is_prime[i]:
                    j = i * i
                    while j <= n:
                        is_prime[j] = False
                        j += i
                i += 1

            return [i for i in range(n+1) if is_prime[i]==True]
        
        primes = prime_sieve(n)
        oprs = 0
        i = 0
        while n > 1:
            if n % primes[i] == 0:
                n = n // primes[i]
                oprs += primes[i]
            else:
                i += 1
        return oprs