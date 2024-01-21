# Write a program to print the multiplication table of a given number.

number = int(input("Provide an integer to provide a multiplication table for: "))
max_multiplier = int(input("Provide the maximum multiplier (as an integer) you would like me to use: "))

for i in range (1, (max_multiplier)+1):
    print(f"{number} * {i} = { (number) * i }")