# Write a program to count the occurrences of a specific character in a string.
appearances = 0
start_index = 0

string_to_count = input("String to count characters in: ")
search_string = input("What shall I search for (note I'm case sensitive)? ")

for i in range(len(string_to_count)):
    my_index = string_to_count.find(search_string,start_index)
    if my_index != -1:
        start_index = my_index + 1
        appearances += 1

if appearances == 1:
    print (f"{search_string} appears {appearances} time in {string_to_count}.")
else:
    print (f'{search_string} appears {appearances} times in "{string_to_count}".')