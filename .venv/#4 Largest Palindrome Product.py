ceiling = 999**2
#find the largest palindrome smaller than n. In this case, we want to find the largest palindrome made from the product of two 3-digit numbers
def largest_palindrome(n):
    result = max(i * j
                 for i in range(100,1000)
                 for j in range(100,1000)
                 if str(i*j)==str(i*j)[::-1])
    return str(result)
print((largest_palindrome(ceiling)))