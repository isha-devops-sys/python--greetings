# Calculator for two numbers

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

addition = a + b
subtraction = a - b
multiplication = a * b

print("Addition =", addition)
print("Subtraction =", subtraction)
print("Multiplication =", multiplication)

if b != 0:
    division = a / b
    print("Division =", division)
else:
    print("Division is not possible because denominator is zero.")
