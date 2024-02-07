# Create a program that removes the nth element from a list.

string_list = input("Enter a series of words separated by spaces\n").split()
nth_element = int(input(f"There are {len(string_list)} elements in the list. What number element shall I remove?\n"))

string_list.remove(string_list[nth_element - 1])

print(string_list)