# Write a program that uses recursion to generate all permutations of a list.

def generate_permutations(sequence, start, end):
    if start == end:
        print(sequence)
    else:
        for i in range(start, end + 1):
            sequence[start], sequence[i] = sequence[i], sequence[start]
            generate_permutations(sequence, start + 1, end)
            sequence[start], sequence[i] = sequence[i], sequence[start]

my_list = ["apple", 2, "igloo", 3]
generate_permutations(my_list, 0, len(my_list) - 1)