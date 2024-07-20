# 2,3,6n-1,6n+1
import sympy

parr = [2,3]
n = 1
while len(parr) <= 10001:
    if sympy.isprime(6*n-1):
        parr.append(6*n-1)
    if sympy.isprime(6*n+1):
        parr.append(6*n+1)
    n+=1
print(parr[10000])

