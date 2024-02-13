# function to check if a number is prime

import math

def check_prime(arg):
    x = int(math.sqrt(arg)) + 1
    values = range(2, x)
    is_prime = True
    for num in values:
        if arg % num == 0:
            is_prime = False
    return(is_prime)

print(check_prime(17))


