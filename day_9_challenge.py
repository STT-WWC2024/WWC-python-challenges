# Write a program to check if a number is even or odd.

while True:
    try:
        num = int(input("Enter an integer: "))
        break
    except ValueError:
        print ("That wasn't an integer, try again!")
even_odd = "odd" if num % 2 == 1 else "even"
print(f"The number {num} is {even_odd}.")