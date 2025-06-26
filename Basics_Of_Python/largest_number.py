a= float(input("Enter first number: "))
b= float(input("Enter second number: "))
c= float(input("Enter third number: "))

def largeNumber(x,y,z):
    if x>=y and x>=z:
        print(f"The largest number is: {x}")
    elif y>=z and y>=x:
        print(f"The largest number is: {y}")
    else:
        print(f"The largest number is: {z}")


largeNumber(a,b,c)