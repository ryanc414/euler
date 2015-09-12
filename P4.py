# largest palindromic product of two 3-digit nums

def is_palindrome(num):
    num_list = [int(d) for d in str(num)]
    return num_list == num_list[::-1]


largest_palindrome = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        product = i * j
        if is_palindrome(product) and product > largest_palindrome:
            largest_palindrome = product

print largest_palindrome
