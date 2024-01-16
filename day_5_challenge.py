# Write a program to find the maximum and minimum values in a list.

list_of_numbers = []
add_to_list = ""
prompt = "Enter a number, enter q to exit entry dialog: "

while add_to_list != 'q':
    add_to_list = input(prompt)
    if add_to_list == 'q':
        print(f"\nMy list is {list_of_numbers}")
        break
    list_of_numbers.append(float(add_to_list))

if len(list_of_numbers) >= 2:
    print(f"The max number is: {max(list_of_numbers)}")
    print(f"The min is: {min(list_of_numbers)}\n")
else:
    print(f"\nI need at least two numbers entered to work. Run me again!\n")