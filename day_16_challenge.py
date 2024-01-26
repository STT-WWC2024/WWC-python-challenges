# Write a function that counts the frequency of each word in a sentence.

import re

def count_unique(str):
    unique_words = []
    no_punctuation_string = re.sub(r'[^\w\s]', '', str)
    string_words = no_punctuation_string.split()
    for item in string_words:
        if unique_words.count(item) == 0:
            unique_words.append(item)
    for word in unique_words:
        if str.count(word) == 1:
            print(f'"{word}" appears {str.count(word)} time')
        else: 
            print(f'"{word}" appears {str.count(word)} times')
        
original_string = input("Enter a string to count each word in: ")
str = original_string.lower()
print(f'In the original string "{original_string}", \n')
count_unique(str)
