# Write a function that accepts a string and calculates the number of uppercase and lowercase letters in it.
import re

def count_letter(str):
    no_caps = re.sub("[A-Z]", "", str)
    no_lower = re.sub("[a-z]", "", str)
    caps = len(str) - len(no_caps)
    lower = len(str) - len(no_lower)
    return caps, lower

str = input("Provide a string that I can count capital and lower case letters from:\n")
uppercase, lowercase = count_letter(str)
print(f"The string has {uppercase} capital letters and {lowercase} lower case letters.")
