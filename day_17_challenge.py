# Create a program that capitalizes the first letter of each word in a sentence

input_string = input('Enter a string: \n')

# Next line "works" but doesn't respect capitalized acronyms and turns them lowercase
# caps_string = ' '.join([word.capitalize() for word in input_string.split()])

letter_list = []

for i in range(0, len(input_string)):
    if i == 0:
        letter_list.append(input_string[i].upper())
    elif (input_string[i - 1]) == " " :
        letter_list.append(input_string[i].upper())
    else:
        letter_list.append(input_string[i])

print(f'\nThe string with the first letter of each word capitalized is: \n"{"".join(letter_list)}"\n')