# Create a program that sorts a list of strings alphabetically.

string_list = input("Enter a series of words separated by spaces\n").split()

print(sorted(string_list, key=lambda x: x.lower()))