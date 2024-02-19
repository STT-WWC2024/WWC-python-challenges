# Write a program to find the most common words in a text file.

import re

top_values = 5
contents = open("./sampletext.txt", "r")
content_list = contents.read().split()
words = []
word_counts = {}
top_words = {}

# make words lowercase and remove non alphanumeric characters
for content in content_list:
    words.append(re.sub(r'[^\w\s]', '', content.lower()))

# count occurences of all words
for word in words:
    if word in word_counts.keys():
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# sort values and put top x values in another dictionary
sorted_word_counts = sorted(word_counts.values())

for i in range(1, top_values+1):
    count_key = [key for key, val in word_counts.items() if val == sorted_word_counts[-(i)]]
    for key in count_key:
        top_words[key] = sorted_word_counts[-(i)]

print(f"Top {top_values} word occurences including ties:")
print(top_words)