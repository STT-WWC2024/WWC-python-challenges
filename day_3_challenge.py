# Write a function to count the number of vowels in a given string
def count_vowels(string_to_count):
    vowel_count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']

    for letter in string_to_count.lower():
        if letter in vowels:
            vowel_count +=1
    
    return vowel_count

string_to_count = input("String to count vowels from: ")
num_vowels = count_vowels(string_to_count)

print (f"There are {num_vowels} vowels in {string_to_count}.")
