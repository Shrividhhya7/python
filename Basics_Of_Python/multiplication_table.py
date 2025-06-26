def multiply():
    n= int(input("Enter a number to multiply: "))
    for i in range(1,11):
        mul = n * i
        print(f"{n} * {i} = {mul}")

multiply()