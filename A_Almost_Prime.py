n = int(input())

count = 0
primes = []

def isPrime(x):
    d = 2
    while d * d <= x:
        if x % d==0:
            return False
        d +=1
    return True


for i in range(2, 3000):
    if isPrime(i):
        primes.append(i)


for i in range(1, n+1):
    c = 0
    for prime in primes:
        if prime < i and i % prime  == 0:
            c += 1
    if c == 2:
        count += 1
print(count)