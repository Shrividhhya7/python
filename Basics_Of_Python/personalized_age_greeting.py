def personalized_greetings():
    name = input("Enter the Name: ")
    age = int(input("Enter the Age: "))
    return f"Hello, {name}! You are {age} years old"

print(personalized_greetings())