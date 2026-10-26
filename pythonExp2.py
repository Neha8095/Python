#IF-ELSE PROGRAMS
#1. Check number is zero or non-zero
n = int(input("Enter a number: "))

if n == 0:
    print("Number is zero")
else:
    print("Number is non-zero")


#Largest of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Largest number =", a)
else:
    print("Largest number =", b)


#Check positive or negative
n = int(input("Enter a number: "))

if n > 0:
    print("Number is positive")
elif n < 0:
    print("Number is negative")
else:
    print("Number is zero")


#4. Check vowel or consonant
ch = input("Enter a character: ")

if ch in "aeiouAEIOU":
    print("It is a vowel")
else:
    print("It is a consonant")

#Student performance

percentage = float(input("Enter percentage: "))

if percentage >= 90:
    print("Excellent performance")
elif percentage >= 80:
    print("Very Good performance")
elif percentage >= 70:
    print("Good performance")
elif percentage >= 60:
    print("Average performance")
else:
    print("Poor performance")

#Largest of three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest =", a)
elif b >= a and b >= c:
    print("Largest =", b)
else:
    print("Largest =", c)

#Check even or odd
n = int(input("Enter a number: "))

if n % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

#Check leap year
year = int(input("Enter year: "))

if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not a leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")

#Driver insurance
age = int(input("Enter age: "))
gender = input("Enter gender (male/female): ")
married = input("Are you married? (yes/no): ")

if married == "yes":
    print("Driver is insured")
elif gender == "male" and age > 30:
    print("Driver is insured")
elif gender == "female" and age > 25:
    print("Driver is insured")
else:
    print("Driver is not insured")


#WHILE LOOP – Below Average
#11. Print natural numbers up to n
n = int(input("Enter n: "))

i = 1

while i <= n:
    print(i)
    i = i + 1

#Print even numbers up to n
n = int(input("Enter n: "))

i = 2

while i <= n:
    print(i)
    i = i + 2

#Print odd numbers up to n
n = int(input("Enter n: "))

i = 1

while i <= n:
    print(i)
    i = i + 2

#Sum of natural numbers up to n
n = int(input("Enter n: "))

i = 1
sum = 0

while i <= n:
    sum = sum + i
    i = i + 1

print("Sum =", sum)

#Sum of odd numbers up to n
n = int(input("Enter n: "))

i = 1
sum = 0

while i <= n:
    sum = sum + i
    i = i + 2

print("Sum of odd numbers =", sum)

#Sum of even numbers up to n
n = int(input("Enter n: "))

i = 2
sum = 0

while i <= n:
    sum = sum + i
    i = i + 2

print("Sum of even numbers =", sum)

#Natural numbers in reverse order
n = int(input("Enter n: "))

while n >= 1:
    print(n)
    n = n - 1

#Fibonacci series up to n terms
n = int(input("Enter number of terms: "))

a = 0
b = 1
i = 1

while i <= n:
    print(a)
    c = a + b
    a = b
    b = c
    i = i + 1

#Factorial of a number
n = int(input("Enter a number: "))

fact = 1
i = 1

while i <= n:
    fact = fact * i
    i = i + 1

print("Factorial =", fact)


#Check whether number is prime
n = int(input("Enter a number: "))

if n < 2:
    print("Not a prime number")
else:
    i = 2
    prime = True

    while i < n:
        if n % i == 0:
            prime = False
            break
        i = i + 1

    if prime:
        print("Prime number")
    else:
        print("Not a prime number")


#Sum of digits
n = int(input("Enter a number: "))

sum = 0

while n > 0:
    digit = n % 10
    sum = sum + digit
    n = n // 10

print("Sum of digits =", sum)

#Check palindrome number
n = int(input("Enter a number: "))

original = n
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

if original == reverse:
    print("Palindrome number")
else:
    print("Not a palindrome number")


#Reverse a number
n = int(input("Enter a number: "))

reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

print("Reverse =", reverse)

#FOR LOOP Programs
#27. Natural numbers up to n

n = int(input("Enter n: "))

for i in range(1, n + 1):
    print(i)

#Even numbers up to n
n = int(input("Enter n: "))

for i in range(2, n + 1, 2):
    print(i)

#Print 1 2 4 8 16 ... n²
#The series in the image is 1, 2, 4, 8, 16, 32... and continues up to the required limit.
n = int(input("Enter n: "))

value = 1

for i in range(n):
    print(value, end=" ")
    value = value * 2

#Sum of series
#1 + 1/1! + 1/2! + 1/3! + ... + 1/n!
n = int(input("Enter n: "))

fact = 1
sum = 1

for i in range(1, n + 1):
    fact = fact * i
    sum = sum + (1 / fact)

print("Sum =", sum)

#Compute cosine series
#The series is:
#cos(x) = 1 − x²/2! + x⁴/4! − x⁶/6! + ...

import math

x = float(input("Enter x: "))
n = int(input("Enter number of terms: "))

sum = 1
sign = -1

for i in range(2, n + 1, 2):
    fact = 1

    for j in range(1, i + 1):
        fact = fact * j

    term = (x ** i) / fact
    sum = sum + sign * term
    sign = sign * -1

print("Cosine value =", sum)

#Check whether square root is prime
#For example, if the number is 49, its square root is 7, and 7 is prime.

import math

n = int(input("Enter a number: "))

root = int(math.sqrt(n))

if root * root != n:
    print("Number is not a perfect square")
else:
    if root < 2:
        print("Square root is not prime")
    else:
        prime = True

        for i in range(2, root):
            if root % i == 0:
                prime = False
                break

        if prime:
            print("Square root is prime")
        else:
            print("Square root is not prime")

#Print ABC pattern
for i in range(3):
    print("A B C")

#Increasing alphabet pattern
#Output for n = 5:

n = int(input("Enter n: "))

for i in range(1, n + 1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()

#Decreasing alphabet pattern
#Output for n = 5:
n = int(input("Enter n: "))

for i in range(n, 0, -1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()

#Increasing number pattern
n = int(input("Enter n: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

#Repeated number pattern
n = int(input("Enter n: "))

for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()