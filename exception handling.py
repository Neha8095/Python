#
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = a / b
    print("Division =", c)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Please enter valid numbers")

#
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print("Result =", a / b)

except ValueError:
    print("Please enter integers only")

except ZeroDivisionError:
    print("Division by zero is not allowed")

except Exception as e:
    print("Error:", e)

#
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a + b

except ValueError:
    print("Invalid input")

else:
    print("Addition =", result)
