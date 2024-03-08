# Create a function that converts a string to an integer and handles ValueError.

def convert_integer(str):
    try:
        int_str = int(str)
        print(f"{str} is now of type: {type(int_str)}")
    except ValueError:
        print("Sorry I can't turn that into a string!")

str = input("Please enter a string for me to turn into an integer:\n")
convert_integer(str)
