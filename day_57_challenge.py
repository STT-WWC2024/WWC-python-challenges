# Create a function that returns the key with the maximum value in a dictionary.

def return_max_value(my_dict):
    return max(my_dict, key=my_dict.get)

d = {"a":1, "b":200, "c":3, "d":50, "e":5, "f":75}

max_val = return_max_value(d)
print(f"The key with maximum value in this dictionary is:\n {max_val}")