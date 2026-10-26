#Function in Python
#Program: Add two numbers using a function

def add(a, b):
    return a + b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

result = add(a, b)

print("Addition =", result)

#Lambda Function
#Program: Find square of a number using lambda

square = lambda x: x * x

n = int(input("Enter a number: "))

result = square(n)

print("Square =", result)



#Array in Python
#Python commonly uses lists for array-like operations. The array module can also be used for a typed array.
#Program: Create and display an array

from array import array

numbers = array('i', [])

n = int(input("Enter number of elements: "))

for i in range(n):
    value = int(input("Enter element: "))
    numbers.append(value)

print("Array elements are:")

for value in numbers:
    print(value, end=" ")


#File Handling
#Program: Create a file and write data into it

file = open("student.txt", "w")

name = input("Enter student name: ")
roll = input("Enter roll number: ")
branch = input("Enter branch: ")

file.write("Name: " + name + "\n")
file.write("Roll Number: " + roll + "\n")
file.write("Branch: " + branch + "\n")

file.close()

print("Data written successfully.")


#File Reading Program
file = open("student.txt", "r")

data = file.read()

print("File contents:")
print(data)

file.close()


#Directory
#Program: Create a directory and display files

import os

directory = input("Enter directory name: ")

if not os.path.exists(directory):
    os.mkdir(directory)
    print("Directory created successfully.")
else:
    print("Directory already exists.")

print("Current directory contents:")

for item in os.listdir("."):
    print(item)


#Module in Python
#A module is a Python file containing functions, variables, or classes that can be used in another Python program.

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

