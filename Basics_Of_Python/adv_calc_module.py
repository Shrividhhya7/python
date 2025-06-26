import calculator as calc


a = float(input("Enter a Number for A: "))  # global variables
b = float(input("Enter a Number for B: "))  # global variables

print("Select Opearation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter choice (1/2/3/4): ")

if choice == '1':
    print("result code:", calc.addition(a,b))
elif choice == '2':
    print("result code:", calc.subtraction(a,b))
elif choice == '3':
    print("result code:", calc.multiplication(a,b))
elif choice == '4':
    print("result code:", calc.division(a,b))
else:
    print("Invalid choice")