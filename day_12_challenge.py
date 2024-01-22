def reverse_string(str):
    if len(str) == 0:
        return str
    else:
        return reverse_string(str[1:]) + str[0]

str = input("Provide a string to reverse: \n")
print("The reverse is: \n")
print(reverse_string(str))