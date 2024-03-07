# Create a function to extract all URLs from a given text using regular expressions.

import re

def extract_urls(str):

    # regex = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    regex = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    url = re.findall(regex, str)

    return url

str = input("Give me a string with one or more URLs:\n")
urls = extract_urls(str)
print(f"The URLs I found are:\n {urls}")