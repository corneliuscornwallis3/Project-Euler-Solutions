# 2,3,6n-1,6n+1
import sympy as sp

total = 5 # 2 and 3 don't follow the formula for primes, so we will at them at the start
n = 1
while 6*n+1 < 2000000:
    p1 = 6*n+1
    p2 = 6*n-1
    if sp.isprime(p1):
        total += p1
    if sp.isprime(p2):
        total += p2
    n += 1
print(total)