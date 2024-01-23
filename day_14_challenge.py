# Write a program to print the first n numbers of a Fibonacci sequence

def print_fibonacci(n):
    
    x = 0
    y = 1

    if n == 0:
        return
    elif n == 1:
        print(x)
        return
    else:
        print(x)
        print(y)
        for i in range ( 3, n + 1):
            print ( x + y )
            new_y = x + y
            x = y
            y = new_y

while True:
    try:
        n = int(input("How many numbers of the Fibonacci sequence shall I print? "))
        break
    except ValueError:
        print ("That wasn't an integer, try again!")

print_fibonacci(n)