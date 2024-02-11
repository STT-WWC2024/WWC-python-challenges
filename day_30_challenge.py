# Create a function that finds the second smallest element in a list.

number_list = []
add_to_list = ""
prompt = "Enter a number or q to exit number entry: "

while add_to_list != 'q':
    try:
        add_to_list = input(prompt)
        if add_to_list == 'q':
            print(f"\nMy list is {number_list}")
            break
        number_list.append(float(add_to_list))
    except ValueError:
        break
print(f"My list is: ")
print(number_list)

print(f"The second largest is: {sorted(number_list, key=int)[1]}")