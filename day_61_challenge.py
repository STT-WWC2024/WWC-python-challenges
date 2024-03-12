# Create a program to implement a stack using a list.

stack = []

def push():
    item = input("Enter an item to add to the stack:\n")
    stack.append(item)
    print(stack)

def pop_item():
    if not stack:
        print("Can't pop from an empty stack!")
    else:
        item = stack.pop()
        print(f'Removed {item}')
        print(stack)

while True:
    to_do = input('What would you like to do? 1 for push, 2 for pop, 3 to quit:\n')
    if to_do == "1":
        push()
    elif to_do == "2":
        pop_item()
    elif to_do == "3":
        break
    else:
        print("I didn't understand that, please type 1, 2, or 3.")

