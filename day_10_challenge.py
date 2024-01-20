# Write a program to remove duplicates from a list.

list = ["apple", "apple", "banana", "cherry", "apple", "banana", "durian"]

# convert to set (loses original order)
deduplicated_set = set(list)

# check if exists in a new list and if not, append to list
deduplicated = []
for item in list:
    if deduplicated.count(item) == 0:
        deduplicated.append(item)
list = deduplicated

print(f"deduplicated list with set: {deduplicated_set}")
print(f"deduplicated list is: {deduplicated}")