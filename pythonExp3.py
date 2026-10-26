#1. String Length Without len()
s = input("Enter a string: ")

count = 0

for ch in s:
    count = count + 1

print("Length of string =", count)

#Count Vowels, Consonants, Digits, Spaces and Special Characters
s = input("Enter a string: ")

vowels = 0
consonants = 0
digits = 0
spaces = 0
special = 0

for ch in s:
    if ch in "aeiouAEIOU":
        vowels = vowels + 1
    elif ch.isalpha():
        consonants = consonants + 1
    elif ch.isdigit():
        digits = digits + 1
    elif ch == " ":
        spaces = spaces + 1
    else:
        special = special + 1

print("Vowels =", vowels)
print("Consonants =", consonants)
print("Digits =", digits)
print("Spaces =", spaces)
print("Special characters =", special)

#Reverse a String Without Built-in Reverse Function
s = input("Enter a string: ")

reverse = ""

for ch in s:
    reverse = ch + reverse

print("Reversed string =", reverse)

#Check Palindrome String
s = input("Enter a string: ")

reverse = ""

for ch in s:
    reverse = ch + reverse

if s == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")

#Count Uppercase and Lowercase Letters
s = input("Enter a string: ")

upper = 0
lower = 0

for ch in s:
    if ch.isupper():
        upper = upper + 1
    elif ch.islower():
        lower = lower + 1

print("Uppercase letters =", upper)
print("Lowercase letters =", lower)

#Replace Characters
s = input("Enter a string: ")

old = input("Enter character to replace: ")
new = input("Enter new character: ")

result = ""

for ch in s:
    if ch == old:
        result = result + new
    else:
        result = result + ch

print("New string =", result)

#Remove All Spaces
s = input("Enter a string: ")

result = ""

for ch in s:
    if ch != " ":
        result = result + ch

print("String without spaces =", result)

#Find Longest Word
s = input("Enter a sentence: ")

words = s.split()

longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word =", longest)

#Find Shortest Word
s = input("Enter a sentence: ")

words = s.split()

shortest = words[0]

for word in words:
    if len(word) < len(shortest):
        shortest = word

print("Shortest word =", shortest)

#Convert to Title Case
s = input("Enter a sentence: ")

words = s.split()
result = ""

for word in words:
    result = result + word[0].upper() + word[1:].lower() + " "

print("Title case =", result)


#Print Duplicate Characters
s = input("Enter a string: ")

duplicates = ""

for ch in s:
    if s.count(ch) > 1 and ch not in duplicates:
        duplicates = duplicates + ch

print("Duplicate characters =", duplicates)

#Frequency of Every Character
s = input("Enter a string: ")

checked = ""

for ch in s:
    if ch not in checked:
        count = 0

        for x in s:
            if x == ch:
                count = count + 1

        print(ch, "=", count)
        checked = checked + ch

#Check Whether Two Strings Are Anagrams
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

s1 = s1.replace(" ", "").lower()
s2 = s2.replace(" ", "").lower()

if sorted(s1) == sorted(s2):
    print("Strings are anagrams")
else:
    print("Strings are not anagrams")

#Remove Duplicate Characters
s = input("Enter a string: ")

result = ""

for ch in s:
    if ch not in result:
        result = result + ch

print("String after removing duplicates =", result)

#Count Occurrences of a Word
sentence = input("Enter a sentence: ")
word = input("Enter word to search: ")

words = sentence.split()

count = 0

for w in words:
    if w == word:
        count = count + 1

print("Occurrences =", count)

#Password Validator
#Conditions from your file:
#- Minimum 8 characters
#- At least one uppercase letter
#- At least one lowercase letter
#- At least one digit
#- At least one special character

password = input("Enter password: ")

upper = False
lower = False
digit = False
special = False

for ch in password:
    if ch.isupper():
        upper = True
    elif ch.islower():
        lower = True
    elif ch.isdigit():
        digit = True
    else:
        special = True

if len(password) >= 8 and upper and lower and digit and special:
    print("Valid password")
else:
    print("Invalid password")

#Run-Length Encoding
#The file gives:
#aaabbccccd → a3b2c4d1

s = input("Enter a string: ")

result = ""
count = 1

for i in range(len(s)):
    if i + 1 < len(s) and s[i] == s[i + 1]:
        count = count + 1
    else:
        result = result + s[i] + str(count)
        count = 1

print("Compressed string =", result)

#String Compression
#Compress the string only if compression makes it shorter; otherwise return the original string.

s = input("Enter a string: ")

compressed = ""
count = 1

for i in range(len(s)):
    if i + 1 < len(s) and s[i] == s[i + 1]:
        count = count + 1
    else:
        compressed = compressed + s[i] + str(count)
        count = 1

if len(compressed) < len(s):
    print("Compressed string =", compressed)
else:
    print("Original string =", s)

#Most Frequent Character
s = input("Enter a string: ")

max_count = 0
max_char = ""

for ch in s:
    count = s.count(ch)

    if count > max_count:
        max_count = count
        max_char = ch

print("Most frequent character =", max_char)
print("Frequency =", max_count)

#Second Most Frequent Character
s = input("Enter a string: ")

frequency = {}

for ch in s:
    if ch in frequency:
        frequency[ch] = frequency[ch] + 1
    else:
        frequency[ch] = 1

values = sorted(frequency.values(), reverse=True)

if len(values) < 2:
    print("Second most frequent character does not exist")
else:
    second = values[1]

    for ch in frequency:
        if frequency[ch] == second:
            print("Second most frequent character =", ch)
            print("Frequency =", second)
            break

#Caesar Cipher – Encryption and Decryption

text = input("Enter message: ")
shift = int(input("Enter shift value: "))

encrypted = ""

for ch in text:
    if ch.isupper():
        encrypted = encrypted + chr((ord(ch) - 65 + shift) % 26 + 65)
    elif ch.islower():
        encrypted = encrypted + chr((ord(ch) - 97 + shift) % 26 + 97)
    else:
        encrypted = encrypted + ch

print("Encrypted message =", encrypted)

decrypted = ""

for ch in encrypted:
    if ch.isupper():
        decrypted = decrypted + chr((ord(ch) - 65 - shift) % 26 + 65)
    elif ch.islower():
        decrypted = decrypted + chr((ord(ch) - 97 - shift) % 26 + 97)
    else:
        decrypted = decrypted + ch

print("Decrypted message =", decrypted)

#String Rotation
#The file asks to check whether one string is a rotation of another, with ABCD and CDAB giving Yes.

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if len(s1) == len(s2) and s2 in (s1 + s1):
    print("Yes, strings are rotations")
else:
    print("No, strings are not rotations")