# Create a function that checks if a number is a perfect square.

import math

def check_square(num):
    sqr_rt = math.sqrt(num)
    if sqr_rt.is_integer() == True:
        return True
    else:
        return False
    
num = float(input("Give me a number:\n"))
is_sqr_rt = check_square(num)
print(f"{num} is a perfect square is {is_sqr_rt}")
    