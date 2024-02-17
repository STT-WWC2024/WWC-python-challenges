# Write a program to iterate through a dictionary and print its keys and values.

my_dict = {"name": "Schmoo",
           "age": 6,
           "weight": "10 lbs",
           "breed": "Brussels Griffon",
           "favorite toy": "noodle nose work toy"}

for key, value in my_dict.items():
    print(f"{key}: {value}")