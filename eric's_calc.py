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
a = int(input("Enter A: "))
b = int(input("Enter B: "))

print(sum(a, b))
print(minus(a, b))
print(multiply(a, b))
print(divide(a, b))