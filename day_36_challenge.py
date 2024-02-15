# Write a Python program to check if two strings are anagrams.
import re

def check_anagrams(string1, string2):

    str1 = re.sub('[\W_]+', '', string1.lower())
    str2 = re.sub('[\W_]+', '', string2.lower())

    anagrams = False

    if len(str1) == len(str2):
        anagrams = True
        for i in range(0, len(str1) - 1):
            if str1.count(str1[i]) != str2.count(str1[i]):
                anagrams = False
                break
    else:
        anagrams = False

    print(f'"{string1}" and "{string2}" are anagrams: {anagrams}')

check_anagrams("Creative", "Reactive")
check_anagrams("The hurricanes", "These churn air")
check_anagrams("To be or not to be: that is the question, whether 'tis nobler in the mind to suffer the slings and arrows of outrageous fortune", "In one of the Bard's best-thought-of tragedies, our insistent hero, Hamlet, queries on two fronts about how life turns rotten.")