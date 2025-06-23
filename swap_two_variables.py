a = int(input("Enter a number for A: "))
b = int(input("Enter a number for B: "))

def swap(a, b):
    temp = a
    a = b
    b = temp
    print(f"a = {a}")
    print(f"b = {b}")

swap(a,b)