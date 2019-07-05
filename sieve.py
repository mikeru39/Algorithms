def sieve(n):
    primes = []
    item = 2
    while len(primes) < n:
        i = [item for i in primes if item % i == 0]
        primes += [] if i else [item]
        item += 1

    return primes[-1]


sieve(10)
# "sieve.sieve(10)"
# 100 loops, best of 5: 35.8 usec per loop

# "sieve.sieve(20)"
# 100 loops, best of 5: 124 usec per loop

# "sieve.sieve(40)"
# 100 loops, best of 5: 476 usec per loop
