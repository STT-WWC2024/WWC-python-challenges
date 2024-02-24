# Write a program that uses a try-except block to handle division by zero.

def divide(num, divisor):
    try:
        print(num/divisor)
    except ZeroDivisionError:
        print("Can't divide by zero, exiting.")
        exit()

num = float(input("Please enter a number: "))
divisor = float(input("Please enter a number to divide by: "))
divide(num, divisor)