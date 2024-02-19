# Write a function to find the largest common divisor of two numbers using a function.

def find_divisor(num1, num2):
    divisors = []

    if num1 > num2:
        x = int(num1/2 + 1)
    else:
        x = int(num2/2 + 1)

    for value in range(1, x):
        if num1 % value == 0 and num2 % value == 0:
            divisors.append(value)

    largest = max(divisors)

    return(largest)

number1 = int(input("Provide an integer: "))
number2 = int(input("Provide a second integer: "))
print(f"The largest common divisor is: {find_divisor(number1, number2)}")