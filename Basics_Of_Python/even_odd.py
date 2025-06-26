num = int(input("Enter a number: "))

def even_odd(number):
    if number % 2 == 0:
        print(f"{number} is even number")
    else:
        print(f"{number} is odd number")


even_odd(num)