sum = 2
prev_1 = 1
prev_2 = 2
while prev_1 + prev_2 < 4000000:
    fib = prev_1 + prev_2
    if fib % 2 == 0:
        sum += fib
    print("prev_1: ",prev_1," prev_2: ",prev_2," fib: ",fib)
    prev_1 = prev_2
    prev_2 = fib

print(sum)