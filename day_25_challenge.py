# Create a program to concatenate two lists.

list1 = [item for item in input("Enter a list of items separated by spaces:\n").split()]
list2 = [item for item in input("Enter a list of items separated by spaces to add to the first list:\n").split()]

concatenated_list = list1 + list2

print(f"My list is: \n")
print(concatenated_list)