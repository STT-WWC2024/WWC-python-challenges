# Write a program to remove vowels from a given string.

import re

def remove_vowels(str):
    no_vowels = re.sub("[aeiouAEIOU]", "", str)
    return no_vowels

str = input("Provide a string that I can remove vowels from:\n")
no_vowels = remove_vowels(str)
print(f"\nThe string without vowels is:\n{no_vowels}")