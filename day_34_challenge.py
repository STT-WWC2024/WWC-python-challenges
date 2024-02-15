# Write a Python program to merge two dictionaries.

first_dict = {"name": "Bob",
         "age": 27,
         "favorite_saying": "skittish as a cat in a room full of rocking chairs"}

second_dict = {"vocal range": "baritone",
         "phone": "555-555-5555"}

merged_dict = {**first_dict, **second_dict}
print(f"Merged with unpacking:\n{merged_dict}")

merged_dict2 = (first_dict | second_dict)
print(f"Merged with | operator:\n{merged_dict2}")

merged_dict3 = first_dict.copy()
merged_dict3.update(second_dict)
print(f"Merged with copy and update:\n{merged_dict3}")

merged_dict4 = first_dict.copy()
for k in second_dict.keys():
    merged_dict4[k] = second_dict[k]
print(f"Merged with copy and for loop:\n{merged_dict4}")