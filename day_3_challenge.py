# Write a function to count the number of vowels in a given string

string_to_count = input("String to count vowels from: ")
vowel_count = 0
vowels = ['a', 'e', 'i', 'o', 'u']

for letter in string_to_count.lower():
    if letter in vowels:
        vowel_count +=1

print (f"There are {vowel_count} vowels in {string_to_count}.")
