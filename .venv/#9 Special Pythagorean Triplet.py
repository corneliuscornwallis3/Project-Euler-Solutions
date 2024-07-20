def pyth_triplet(product):
    a = 1
    while True:
        for b in range(a+1,product):
            for c in range(b+1,product):
                if a**2+b**2 == c**2 and a+b+c == 1000:
                    return a*b*c
        a += 1

print(pyth_triplet(1000))