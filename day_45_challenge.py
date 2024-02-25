# Write a function to check if a number is a prime number.

import math

def check_prime(arg):

    if arg == 1:
        return(True)
        exit()

    x = int(math.sqrt(arg)) + 1
    values = range(2, x)
    is_prime = True

    for num in values:
        if arg % num == 0:
            is_prime = False

    return(is_prime)

try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("That was not an integer. Exiting.")
    exit()

check_prime(num)
print(f"{num} is prime: {check_prime(num)}")