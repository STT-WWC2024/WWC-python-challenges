import time

var1 = input('\nPlease provide a value for variable 1: ')
var2 = input('Please provide a value for variable 2: ')

print(f"\nVariable 1 is currently {var1}.")
print(f"Variable 2 is currently {var2}.")
print("\n\nMAGIC HAPPENING HERE\n\n")
time.sleep(1)

temp_var1 = var1
var1 = var2
var2 = temp_var1

print(f"Variable 1 is now {var1}")
print(f"Variable 2 is now {var2}")