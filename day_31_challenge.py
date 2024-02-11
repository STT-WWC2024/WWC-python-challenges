# Create a program that checks if a given string is a valid email address.

import re

email_match = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

def validate_email(email):
    if re.fullmatch(email_match, email):
        print("This looks like a valid e-mail address.")
    else:
        print("That does not look like an e-mail address.")

email = input("Enter a string and I'll check if it's an e-mail:\n")
validate_email(email)