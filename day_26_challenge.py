# Create a program that uses a lambda function to square each element of a list.

list_nums = [1, 2, 3, 4, 5]

square_num = lambda x: x**2

for item in list_nums:
    print(square_num(item))
