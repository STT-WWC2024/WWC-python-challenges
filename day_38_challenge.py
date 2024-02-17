# Write a program to flatten a nested list

nested_list = [["apple", "pear"], "banana", ["apricot", "plum", "cherry"], "durian"]
flattened_list = []

for fruit in nested_list:
    if type(fruit) != list:
        flattened_list.append(fruit)
    elif type(fruit) == list:
        for each in fruit:
            flattened_list.append(each)

print(flattened_list)