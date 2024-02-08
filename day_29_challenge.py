# Create a function that generates a random number between a given range.

import random

def generate_num(x, y):
    return random.randint(x,y)

try:
    x = int(input("""Let's generate a random number in a range.
Give me a starting integer:\n"""))
except ValueError:
    print("Please enter integers only!")
    exit()

try:
    y = int(input("What is the last integer of the range?\n"))
except ValueError:
    print("Please enter integers only!")
    exit()

if x >= y:
    print("The first number needs to be less than the second number.")
    exit()
else:
    print(f"My random number is:\n{generate_num(x, y)}")
