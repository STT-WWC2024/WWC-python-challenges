# Create a program that replaces specific words in a text with their synonyms.

from nltk.corpus import wordnet
import random

file = open("sample.txt")
sample_text = file.read()
word_to_replace = "travel"

def find_synonym(word_to_replace):
    synonyms = []
    for syn in wordnet.synsets(word_to_replace):
        for lm in syn.lemmas():
            if lm.name() != word_to_replace:
                synonyms.append(lm.name())
    return(random.choice(synonyms))

new_word = find_synonym(word_to_replace)

print(f'New text replacing "{word_to_replace}" with "{new_word}":\n{sample_text.replace(word_to_replace, new_word)}')