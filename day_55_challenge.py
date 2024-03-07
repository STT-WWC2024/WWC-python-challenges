# Create a function that takes a string and returns the reverse of each word

def reverse_words(str):
    words = str.split()
    reverses = []
    for word in words:
        rev_word = ''.join([*word][::-1])
        reverses.append(rev_word)
    return reverses

str = input("Give me a string:\n")
reverse_str = reverse_words(str)
print(f"The reverse of each word is as follows:\n {reverse_str}")