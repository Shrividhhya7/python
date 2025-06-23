def factorial():
    n = int(input("Enter a Number: "))
    fact =1
    if n < 0:
        print("Factorial is not defined for negative number")
        return
    
    for i in range (1, n+1):
        fact *=i
    print(f"Factorial of {n} is {fact}")


factorial()