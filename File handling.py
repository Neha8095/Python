#Create student.txt and write student details
file = open("student.txt", "w")

name = input("Enter student name: ")
roll = input("Enter roll number: ")
branch = input("Enter branch: ")
semester = input("Enter semester: ")

file.write("Name: " + name + "\n")
file.write("Roll Number: " + roll + "\n")
file.write("Branch: " + branch + "\n")
file.write("Semester: " + semester + "\n")

file.close()

print("Student details written successfully.")

#Display complete contents of a text file
file = open("student.txt", "r")

data = file.read()

print("File Contents:")
print(data)

file.close()

#Append additional information without deleting previous contents

file = open("student.txt", "a")

info = input("Enter additional information: ")

file.write(info + "\n")

file.close()

print("Information appended successfully.")

#Read a file line by line

file = open("student.txt", "r")

print("File contents line by line:")

for line in file:
    print(line.strip())

file.close()

#Count total number of lines
file = open("student.txt", "r")

lines = file.readlines()

print("Total number of lines:", len(lines))

file.close()

#Count total number of words

file = open("student.txt", "r")

data = file.read()

words = data.split()

print("Total number of words:", len(words))

file.close()


#Count total characters including spaces

file = open("student.txt", "r")

data = file.read()

print("Total number of characters:", len(data))

file.close()

#Display lines in reverse order

file = open("student.txt", "r")

lines = file.readlines()

print("Lines in reverse order:")

for line in reversed(lines):
    print(line.strip())

file.close()


#Count vowels and consonants

file = open("student.txt", "r")

data = file.read()

vowels = 0
consonants = 0

for ch in data:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Number of vowels:", vowels)
print("Number of consonants:", consonants)

file.close()


#Count alphabets, digits, spaces and special characters


file = open("student.txt", "r")

data = file.read()

alphabets = 0
digits = 0
spaces = 0
special = 0

for ch in data:
    if ch.isalpha():
        alphabets += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1
    elif ch != "\n":
        special += 1

print("Alphabets:", alphabets)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)

file.close()

