# Write a program to shuffle the elements of a list randomly.

import random

str_list = ['mango', 'durian', 'mangosteen', 'plantain', 'jackfruit']

rand_list = random.sample(str_list, len(str_list))

print(f"Original list: {str_list}")
print(f"Randomized list: {rand_list}")