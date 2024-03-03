# Create a program that counts the occurrences of each word in a text file.

import re

contents = open("./sampletext.txt", "r")
content_list = contents.read().split()
words = []
word_counts = {}

# make words lowercase and remove non alphanumeric characters
for content in content_list:
    words.append(re.sub(r'[^\w\s]', '', content.lower()))

# count occurences of all words
for word in words:
    if word in word_counts.keys():
        word_counts[word] += 1
    else:
        word_counts[word] = 1

sorted_words = sorted(word_counts.items(), key=lambda x:x[1], reverse=True)

print(f"Count of each word in file:")
for key, value in sorted_words:
    print((key,value))
