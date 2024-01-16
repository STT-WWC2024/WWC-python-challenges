# Write a program to find the sum of all elements in a list.

list_to_sum = []
sum_of_list = 0
number_to_add = ""
prompt = "Enter a number, enter q to exit entry dialog: "

while number_to_add != 'q':
    number_to_add = input(prompt)
    if number_to_add == 'q':
        print(f"\nMy list to sum up is {list_to_sum}")
        break
    list_to_sum.append(float(number_to_add))

for number in list_to_sum:
    sum_of_list = sum_of_list + number

print(f"These add up to {sum_of_list}\n")