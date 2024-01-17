# Write a program to check if a number is positive, negative, or zero.

while True:
    try:
        num = float(input("Please enter a number: "))
        break
    except ValueError:
        print("""That doesn't seem to be a number. You didn't include commas, did you?\nTry again... """)

def sign_or_zero(num):
    if num == 0:
        return "zero"
    return "negative" if num < 0 else "positive"

print(f"{num} is {sign_or_zero(num)}")