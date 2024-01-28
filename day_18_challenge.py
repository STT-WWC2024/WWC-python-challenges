# Create a program to find the largest among three numbers.

number_list = input("Enter three numbers separated by spaces: ").split()
print(sorted(number_list, key=int)[-1])