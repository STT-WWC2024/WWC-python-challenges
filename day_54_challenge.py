# Create a function to find all words in a sentence that start with a vowel.

import re

def find_vowel_starts(str):
    words = str.split()
    vowel_words = []
    regex = '^[aeiouAEIOU][A-Za-z0-9_]*'

    for word in words:
        if(re.search(regex, word)):
            stripped_word = re.sub(r'[^\w\s]', '', word)
            vowel_words.append(stripped_word.lower())
    
    return set(vowel_words)

str = input("Enter a sentence that has some words that start with vowels:\n")

vowel_words = find_vowel_starts(str)

print("The words that start with vowels are:")

for word in vowel_words:
    print(word)