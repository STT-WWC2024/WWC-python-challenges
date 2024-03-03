# Create a program that checks if a string is a palindrome.

import math
import re

string = "A dog! A panic in a pagoda!"
cleaned_string = re.sub(r'[\W_]', '', string.lower())
string_letters = list(cleaned_string)
compare_length = math.floor(len(string_letters)/2)

is_palindrome = False
for i in range(0, compare_length + 1):
    if string_letters[i] == string_letters[-(i+1)]:
        is_palindrome = True
    else:
        is_palindrome = False

print(f'"{string}" is a palindrome: {is_palindrome}')
