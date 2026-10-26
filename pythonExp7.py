#1. Addition of Two Numbers Using a Function
def add(a, b):
    return a + b

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

result = add(x, y)
print("Addition =", result)


#2. Find the Square of a Number
def square(n):
    return n * n

num = int(input("Enter a number: "))
print("Square =", square(num))



#3. Check Whether a Number Is Even or Odd
def check(n):
    if n % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

num = int(input("Enter a number: "))
check(num)


#4. Find the Factorial of a Number
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

num = int(input("Enter a number: "))
print("Factorial =", factorial(num))



#5. Find the Largest of Two Numbers
def largest(a, b):
    if a > b:
        return a
    else:
        return b

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Largest number =", largest(x, y))



#6. Check Whether a Number Is Prime
def prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

num = int(input("Enter a number: "))

if prime(num):
    print("Prime number")
else:
    print("Not a prime number")


#7. Find the Sum of Natural Numbers
def sum_n(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total

num = int(input("Enter a number: "))
print("Sum =", sum_n(num))


#8. Function With a Default Argument
def greet(name="Student"):
    print("Hello", name)

greet()
greet("Rahul")




#9. Find the Area of a Rectangle
def area(length, breadth):
    return length * breadth

l = int(input("Enter length: "))
b = int(input("Enter breadth: "))

print("Area of rectangle =", area(l, b))



#10. Swap Two Numbers Using a Function
def swap(a, b):
    a, b = b, a
    print("After swapping:", a, b)

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

swap(x, y)

