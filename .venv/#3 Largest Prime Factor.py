import math
import sympy

def smallest_prime(n):
    assert n>= 2
    for i in range(2, math.isqrt(n)+1):
        if n % i == 0:
            return i
    return n

def main():
    n = 600851475143
    while True:
        p = smallest_prime(n)
        if p < n:
            n //= p
        else:
            return str(n)

print(main())