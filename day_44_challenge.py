# Write a program that reads an integer from the user and handles invalid inputs.
num = None
while type(num) != int:
    try:
        num = int(input("Enter an integer: "))
    except ValueError:
        print("That was not an integer. Try again!")

print(f"Yay! {num} is an integer!")
