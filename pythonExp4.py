#1. Student Grade Management System
students = []
grades = []

def add_student():
    name = input("Enter student name: ")
    grade = float(input("Enter grade: "))

    students.append(name)
    grades.append(grade)

    print("Student added successfully.")

def update_grade():
    name = input("Enter student name: ")

    if name in students:
        index = students.index(name)
        grade = float(input("Enter new grade: "))
        grades[index] = grade
        print("Grade updated successfully.")
    else:
        print("Student not found.")

def remove_student():
    name = input("Enter student name: ")

    if name in students:
        index = students.index(name)
        students.pop(index)
        grades.pop(index)
        print("Student removed.")
    else:
        print("Student not found.")

def display_average():
    if len(grades) > 0:
        average = sum(grades) / len(grades)
        print("Average grade =", average)
    else:
        print("No grades available.")

def display_extreme():
    if len(grades) > 0:
        print("Highest grade =", max(grades))
        print("Lowest grade =", min(grades))
    else:
        print("No grades available.")

add_student()
add_student()

print("\nStudents:", students)
print("Grades:", grades)

display_average()
display_extreme()

update_grade()
remove_student()

print("\nFinal Students:", students)
print("Final Grades:", grades)

#Points in 2D Plane Using Tuples
import math

points = [(2, 3), (5, 7), (1, 1), (8, 4)]

def distance(p1, p2):
    x = p2[0] - p1[0]
    y = p2[1] - p1[1]

    return math.sqrt(x * x + y * y)

def farthest_point(points):
    farthest = points[0]
    max_distance = math.sqrt(
        farthest[0] ** 2 + farthest[1] ** 2
    )

    for point in points:
        d = math.sqrt(point[0] ** 2 + point[1] ** 2)

        if d > max_distance:
            max_distance = d
            farthest = point

    return farthest

print("Points:", points)

p1 = points[0]
p2 = points[1]

print("Distance =", distance(p1, p2))

print("Farthest point from origin =",
      farthest_point(points))

#Web Server Configuration Using Tuple and List
server_ip = ("192.168.1.10",)
allowed_ips = ["192.168.1.20", "192.168.1.30"]

def update_allowed_ip():
    ip = input("Enter new allowed IP: ")
    allowed_ips.append(ip)
    print("IP added successfully.")

print("Server IP:", server_ip)
print("Allowed IPs:", allowed_ips)

update_allowed_ip()

print("\nUpdated Configuration")
print("Server IP:", server_ip)
print("Allowed IPs:", allowed_ips)

# Employee Projects Using Sets
project1 = {"Amit", "Rahul", "Sneha", "Priya"}
project2 = {"Rahul", "Priya", "Neha", "Kiran"}

print("Project 1 employees:", project1)
print("Project 2 employees:", project2)

print("\nEmployees working on both projects:")
print(project1.intersection(project2))

print("\nEmployees only in Project 1:")
print(project1.difference(project2))

print("\nEmployees only in Project 2:")
print(project2.difference(project1))

print("\nAll unique employees:")
print(project1.union(project2))

#Text Analysis Tool
text = input("Enter a paragraph: ")

words = text.lower().split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("\nTotal number of words =", len(words))

print("\nWord Frequency:")
for word in frequency:
    print(word, "=", frequency[word])

sorted_words = sorted(
    frequency.items(),
    key=lambda x: x[1],
    reverse=True
)

print("\nTop 3 most frequent words:")
for word, count in sorted_words[:3]:
    print(word, "=", count)

vowels = 0

for ch in text.lower():
    if ch in "aeiou":
        vowels += 1

print("\nTotal vowels =", vowels)

#Vocabulary Analysis of Two Books
book1 = input("Enter text of Book 1: ")
book2 = input("Enter text of Book 2: ")

words1 = set(book1.lower().split())
words2 = set(book2.lower().split())

print("\nUnique words in Book 1:")
print(words1)

print("\nUnique words in Book 2:")
print(words2)

print("\nCommon words:")
print(words1.intersection(words2))

print("\nWords unique to Book 1:")
print(words1.difference(words2))

print("\nWords unique to Book 2:")
print(words2.difference(words1))

all_words = words1.union(words2)

print("\nTotal unique words =", len(all_words))

#Store Inventory System
inventory = {}

def add_product():
    name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))

    inventory[name] = quantity
    print("Product added.")

def update_product():
    name = input("Enter product name: ")

    if name in inventory:
        quantity = int(input("Enter new quantity: "))
        inventory[name] = quantity
        print("Quantity updated.")
    else:
        print("Product not found.")

def remove_product():
    name = input("Enter product name: ")

    if name in inventory:
        if inventory[name] == 0:
            del inventory[name]
            print("Product removed.")
        else:
            print("Product quantity is not zero.")
    else:
        print("Product not found.")

def highest_stock():
    if inventory:
        product = max(inventory, key=inventory.get)
        print("Highest stock product:", product)
        print("Quantity:", inventory[product])

add_product()
add_product()

print("\nInventory:", inventory)

update_product()
highest_stock()

print("Total unique products =", len(inventory))

#Anagram Check
import string

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

s1 = s1.lower()
s2 = s2.lower()

result1 = ""
result2 = ""

for ch in s1:
    if ch.isalnum():
        result1 += ch

for ch in s2:
    if ch.isalnum():
        result2 += ch

if sorted(result1) == sorted(result2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")


#Weekly Attendance System
attendance = {
    "Monday": {"Amit", "Rahul", "Sneha"},
    "Tuesday": {"Amit", "Rahul", "Priya"},
    "Wednesday": {"Amit", "Rahul", "Sneha"},
    "Thursday": {"Amit", "Rahul"},
    "Friday": {"Amit", "Rahul", "Priya"}
}

all_students = set()

for students in attendance.values():
    all_students = all_students.union(students)

all_days_students = set(attendance["Monday"])

for students in attendance.values():
    all_days_students = all_days_students.intersection(students)

count = {}

for students in attendance.values():
    for student in students:
        if student in count:
            count[student] += 1
        else:
            count[student] = 1

one_class = set()

for student in count:
    if count[student] == 1:
        one_class.add(student)

print("Students attending all classes:")
print(all_days_students)

print("\nStudents attending only one class:")
print(one_class)

print("\nTotal unique students:",
      len(all_students))


#Character Frequency in Descending Order
text = input("Enter a string: ")

choice = input("Ignore case? (yes/no): ")

if choice.lower() == "yes":
    text = text.lower()

frequency = {}

for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

sorted_frequency = sorted(
    frequency.items(),
    key=lambda x: x[1],
    reverse=True
)

print("\nCharacter Frequency:")

for ch, count in sorted_frequency:
    print(repr(ch), "=", count) = input("Enter a string: ")

choice = input("Ignore case? (yes/no): ")

if choice.lower() == "yes":
    text = text.lower()

frequency = {}

for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

sorted_frequency = sorted(
    frequency.items(),
    key=lambda x: x[1],
    reverse=True
)

print("\nCharacter Frequency:")

for ch, count in sorted_frequency:
    print(repr(ch), "=", count)

#Email Validator Using Regular Expression
import re

email = input("Enter email address: ")

pattern = r'^[A-Za-z0-9._-]+@[A-Za-z0-9]+\.[A-Za-z]{2,6}$'

if re.match(pattern, email):
    print("Valid email address")
else:
    print("Invalid email address")


#Extract Phone Numbers
import re

text = input("Enter text: ")

pattern = r'(?:\(\d{3}\)\s\d{3}-\d{4}|\d{3}-\d{3}-\d{4}|\d{3}\.\d{3}\.\d{4}|\d{10})'

numbers = re.findall(pattern, text)

print("Phone numbers found:")

for number in numbers:
    print(number)

#Extract URLs from HTML
import re

html = input("Enter HTML content: ")

pattern = r'(?:https?://|www\.)[A-Za-z0-9.-]+\.[A-Za-z]{2,}(?:/[^\s<>"]*)?'

urls = re.findall(pattern, html)

print("URLs found:")

for url in urls:
    print(url)


#Multilevel Inheritance – Person → Employee → Manager
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Employee(Person):

    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

    def display_employee_info(self):
        self.display_person_info()
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)


class Manager(Employee):

    def __init__(
        self,
        name,
        age,
        employee_id,
        salary,
        department,
        team_size
    ):
        super().__init__(
            name,
            age,
            employee_id,
            salary
        )

        self.department = department
        self.team_size = team_size

    def display_manager_info(self):
        self.display_employee_info()
        print("Department:", self.department)
        print("Team Size:", self.team_size)


manager = Manager(
    "Neha",
    30,
    "M101",
    60000,
    "Computer Science",
    10
)

manager.display_manager_info()


#Calculator – Default Arguments
class Calculator:

    def add(self, a, b, c=0, d=0):
        return a + b + c + d


calc = Calculator()

print("Addition of 2 numbers:",
      calc.add(10, 20))

print("Addition of 3 numbers:",
      calc.add(10, 20, 30))

print("Addition of 4 numbers:",
      calc.add(10, 20, 30, 40))






