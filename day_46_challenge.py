# Write a function to check if a given list is sorted.

def check_sorted(orig_list):
    new_list = sorted(orig_list)
    if orig_list == new_list:
        orig_sorted = True
    else:
        orig_sorted = False
    return orig_sorted

list1 = ["durian", "banana", "apple", "fig"]
print(f"list1 is sorted: {check_sorted(list1)}")

list2 = ["apple", "banana", "durian", "fig"]
print(f"list2 is sorted: {check_sorted(list2)}")