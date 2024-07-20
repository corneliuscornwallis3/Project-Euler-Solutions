sum_squared = 0
squared_sum = 0
for i in range(101):
    sum_squared += i**2
    squared_sum += i
print(squared_sum**2-sum_squared)