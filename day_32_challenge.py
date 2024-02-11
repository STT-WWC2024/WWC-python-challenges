# Create a function that calculates the average of a list of numbers

number_list = []
add_to_list = ""

def calculate_average(number_list):
    total = 0
    for num in number_list:
        total += num
    return total/len(number_list)

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

avg = calculate_average(number_list)

print(f"The average is: {avg}\n")