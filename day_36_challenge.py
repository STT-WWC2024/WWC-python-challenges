# Write a Python program to check if two strings are anagrams.

string1 = "The hurricanes"
string2 = "These churn air"

str1 = string1.replace(" ", "").lower()
str2 = string2.replace(" ", "").lower()

anagrams = False

if len(str1) == len(str2):
    anagrams = True
    for i in range(0, len(str1) - 1):
        if str1.count(str1[i].lower()) != str2.count(str1[i].lower()):
            anagrams = False
            break

else:
    anagrams = False

print(f"{string1} and {string2} are anagrams: {anagrams}")