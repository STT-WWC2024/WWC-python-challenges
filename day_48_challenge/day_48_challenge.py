# Create a program that replaces specific words in a text with their synonyms.

from nltk.corpus import wordnet

file = open("sample.txt")
sample_text = file.read()
to_replace = "travel"
synonyms = []

for syn in wordnet.synsets(to_replace):
    for lm in syn.lemmas():
        if lm.name() != to_replace:
             synonyms.append(lm.name())

print(f"Synonyms for {to_replace}: {synonyms}")

for word in synonyms:
    print(f"\nsynonym = {word}:")
    new_sentence = sample_text.replace(to_replace, word)
    print(new_sentence)