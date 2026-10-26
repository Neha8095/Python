#1. Email Checking using Regular Expression

import re

email = input("Enter email: ")

pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

if re.match(pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")

#Password Checking using Regular Expression

import re

password = input("Enter password: ")

pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%!]).{8,}$'

if re.match(pattern, password):
    print("Valid Password")
else:
    print("Invalid Password")


#Phone Number Checking using Regular Expression
#For an Indian 10-digit mobile number beginning with 6, 7, 8, or 9:

import re

phone = input("Enter phone number: ")

pattern = r'^[6-9][0-9]{9}$'

if re.match(pattern, phone):
    print("Valid Phone Number")
else:
    print("Invalid Phone Number")


#re.match() Example
#match() checks the pattern only at the beginning of the string.

import re

text = "Python is easy"

result = re.match(r'Python', text)

if result:
    print("Pattern matched")
    print("Matched text:", result.group())
else:
    print("Pattern not matched")


#re.findall() Example
#findall() finds all occurrences of a pattern in a string.

import re

text = "Python, Java, Python, C++, Python"

result = re.findall(r'Python', text)

print("Found:", result)
print("Number of occurrences:", len(result))