# Write a function to calculate the factorial of a number.

# uncomment the next two lines if you really want to get around the max recursion depth
# import sys
# sys.setrecursionlimit(10**6)

def num_factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * num_factorial(n - 1)

try:
    num = int(input("Enter a positive integer (less than 1000 please!) "))
    if num > 999 or num < 0:
        exit()
except ValueError:
    print("That wasn't an integer!")
    exit()

print(num_factorial(num))