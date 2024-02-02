# Create a program to remove a specific element from a set.

my_set = {"hamburger", "cheeseburger", "pizza", "nachos", "chef's salad"}
print(f"I have these items: \n{my_set}")
unwanted_item = input("Select one item to remove: \n")
my_set.discard(unwanted_item)
print(f"The set is now: \n{my_set}")