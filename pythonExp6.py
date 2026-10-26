
# BankAccount – Deposit, Withdraw and Transfer

class BankAccount:
    account_counter = 1000

    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0
        BankAccount.account_counter += 1
        self.account_number = BankAccount.account_counter

    def deposit(self, amount):
        self.balance += amount
        print(amount, "deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(amount, "withdrawn successfully.")
        else:
            print("Error: Insufficient balance.")

    def display_balance(self):
        print("Account Holder:", self.account_holder)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)

    def transfer(self, amount, other_account):
        if amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount
            print(amount, "transferred successfully.")
        else:
            print("Error: Insufficient balance for transfer.")


# Create two accounts
account1 = BankAccount("Rahul")
account2 = BankAccount("Priya")

# Deposit money
account1.deposit(5000)
account2.deposit(3000)

# Display balances
print("\n--- Initial Account Details ---")
account1.display_balance()
account2.display_balance()

# Withdraw money
print("\n--- Withdrawal ---")
account1.withdraw(1000)

# Transfer money
print("\n--- Transfer ---")
account1.transfer(1500, account2)

# Final balances
print("\n--- Final Account Details ---")
account1.display_balance()
account2.display_balance()

#Person and Employee – Single Inheritance

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
        print("\n--- Employee Details ---")

        # Calling parent class method
        self.display_person_info()

        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)


# Create Employee object
employee = Employee("Neha", 21, "EMP101", 35000)

# Display employee information
employee.display_employee_info()


#Multilevel Inheritance – Person → Employee → Manage

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
        print("\n--- Employee Details ---")

        # Calling Person class method
        self.display_person_info()

        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)


class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department, team_size):
        super().__init__(name, age, employee_id, salary)
        self.department = department
        self.team_size = team_size

    def display_manager_info(self):
        print("\n--- Manager Details ---")

        # Calling Employee method
        self.display_employee_info()

        print("Department:", self.department)
        print("Team Size:", self.team_size)


# Create Manager object
manager = Manager(
    "Priya",
    35,
    "MGR101",
    75000,
    "Computer Science",
    10
)

# Display complete manager information
manager.display_manager_info()

#1. Constructor and Destructor

class Student:

    # Constructor
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        print("Constructor called")
        print("Student object created")

    # Destructor
    def __del__(self):
        print("Destructor called")
        print("Student object destroyed")


# Create object
student = Student("Neha", 101)

print("Student Name:", student.name)
print("Roll Number:", student.roll_no)

# Destructor will be called when object is deleted
del student

print("Program ended")



#2. Single Inheritance
#Single inheritance: One child class inherits from one parent class.

class Person:

    def display_person(self):
        print("Name: Neha")
        print("Age: 21")


class Student(Person):

    def display_student(self):
        print("Roll Number: 101")
        print("Branch: Computer Science")


# Create object of Student
student = Student()

student.display_person()
student.display_student()

#3. Multiple Inheritance
#Multiple inheritance: One child class inherits from more than one parent class.

class Father:

    def father_info(self):
        print("Father Name: Raj")


class Mother:

    def mother_info(self):
        print("Mother Name: Priya")


class Child(Father, Mother):

    def child_info(self):
        print("Child Name: Neha")


# Create object
child = Child()

child.father_info()
child.mother_info()
child.child_info()


#Hierarchical Inheritance
#Hierarchical inheritance: Multiple child classes inherit from the same parent class.

class Person:

    def person_info(self):
        print("Name: Neha")
        print("Age: 21")


class Student(Person):

    def student_info(self):
        print("Roll Number: 101")
        print("Branch: CSE")


class Teacher(Person):

    def teacher_info(self):
        print("Subject: Python")
        print("Experience: 5 Years")


# Student object
print("--- Student Details ---")
student = Student()
student.person_info()
student.student_info()

# Teacher object
print("\n--- Teacher Details ---")
teacher = Teacher()
teacher.person_info()
teacher.teacher_info()

#Hybrid Inheritance
#Hybrid inheritance is a combination of two or more types of inheritance.
#Here we combine hierarchical + multiple inheritance.

class Person:

    def person_info(self):
        print("Name: Neha")
        print("Age: 21")


class Student(Person):

    def student_info(self):
        print("Roll Number: 101")
        print("Branch: CSE")


class Teacher(Person):

    def teacher_info(self):
        print("Subject: Python")


class TeachingAssistant(Student, Teacher):

    def ta_info(self):
        print("Role: Teaching Assistant")


# Create object
ta = TeachingAssistant()

ta.person_info()
ta.student_info()
ta.teacher_info()
ta.ta_info()

#Private and Protected Variables and Functions in Multilevel Inheritance
class Person:

    def __init__(self):
        self._name = "Neha"          # Protected variable
        self.__age = 21              # Private variable

    def _display_name(self):         # Protected function
        print("Name:", self._name)

    def __display_age(self):         # Private function
        print("Age:", self.__age)

    def display_person(self):
        self._display_name()
        self.__display_age()


class Employee(Person):

    def __init__(self):
        super().__init__()
        self._salary = 35000          # Protected variable
        self.__employee_id = "E101"   # Private variable

    def _display_salary(self):        # Protected function
        print("Salary:", self._salary)

    def __display_employee_id(self):  # Private function
        print("Employee ID:", self.__employee_id)

    def display_employee(self):
        self.display_person()
        self._display_salary()
        self.__display_employee_id()


class Manager(Employee):

    def __init__(self):
        super().__init__()
        self._department = "IT"       # Protected variable
        self.__team_size = 10         # Private variable

    def _display_department(self):    # Protected function
        print("Department:", self._department)

    def __display_team_size(self):    # Private function
        print("Team Size:", self.__team_size)

    def display_manager(self):
        self.display_employee()
        self._display_department()
        self.__display_team_size()


# Create Manager object
manager = Manager()

print("--- Manager Details ---")
manager.display_manager()
