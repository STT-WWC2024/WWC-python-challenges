# Write a program that checks if a key exists in a dictionary.

dog = {
    "name": "Schmoo",
    "breed": "Brussels Griffon",
    "color": "black",
    "age": "6",
    "weight": "10.2 lbs",
    "favorite treat": "chicken",
    "favorite toy": "noodle nosework game",
}

search_key = input("What key shall I search for? ").lower()

if search_key in dog:
    print(f'\nYes, search key "{search_key}" is in this dictionary.')
    print(f"Its value is {dog[search_key]}.\n")
else:
    print(f"\nI don't have {search_key} in my dictionary.\n")