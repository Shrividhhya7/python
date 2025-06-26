a = int(input("Enter a Number for A: "))  # global variables
b = int(input("Enter a Numbercfor B: "))  # global variables

# addition of two numbers
def addition():
    c = int(input("Enter a Number for C: ")) # local variables
    x = a + b + c
    print("Addition of two number is:", x)
addition()

#  subtraction of two numbers
def subtraction():
    y = a - b
    print("Subtraction of two numbers is:", y)
subtraction()
