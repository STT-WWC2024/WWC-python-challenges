# Write a program that removes all whitespaces from a given string.

import re

def remove_whitespace(str):
    no_spaces = re.sub(r"\s+", "", str)
    return no_spaces

str = input("Enter a string to remove whitespace from: ")
print(remove_whitespace(str))