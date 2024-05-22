def sum(a,b):
    return a +b
def minus(a, b):
    return a -b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error: cannot divide by zero"
    return a // b
def exponent(a, b):
    return a ** b
try:
     a = int(input("Enter A: "))
     b = int(input("Enter B: "))

     print(f"Sum: {sum(a, b)}")
     print(f"Difference: {minus(a, b)}")
     print(f"Product: {multiply(a, b)}")
     print(f"Quotient: {divide(a, b)}")
     print(f"Exponent: {exponent(a, b)}")
except ValueError:
    print("Error: please enter valid numbers")



