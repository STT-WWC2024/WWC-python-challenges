# Write a function that takes a list of numbers and returns a new list containing only the even numbers.

def find_evens(input_list):
    evens = []
    for num in input_list:
        if int(num) % 2 == 0:
            evens.append(num)
    return evens
    
input_list = input("""Enter a list of numbers separated with spaces.
I will return the even numbers: """).split()

result = find_evens(input_list)
print(result)