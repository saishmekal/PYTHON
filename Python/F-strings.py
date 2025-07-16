#F-STRING FOR VARIABLES
name = "Saish"
age = 20
print(f"My name is {name} and I'm {age} years old")


#F-STRING FOR EXPRESSIONS
a = 10
b = 17
print(f"The Addition of these numbers will be {a+b}")


#F-STRING FOR FUNCTIONS CALLED INSIDE F-SRTINGS
def greet(name):
    return f"Hello, {name}!"

print(f"Custom Message: {greet('Saish')}")


#String Formatting (Alignment, Precision, etc.)
name = "Saish"
print(f"{name:>10}") #Right align
print(f"{name:<10}") #Left align
print(f"{name:^10}") #Center align


# Number Formatting
pi = 3.145926
large_number = 123456789

# Decimal precision
print(f"The 2 numbers after decimal in pi is {pi:.2f}")

# Comma as a thousands separator
print(f"The commas for thousands for large number is {large_number:,}")