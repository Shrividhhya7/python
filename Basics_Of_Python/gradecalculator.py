num = float(input("Enter a score: "))

def grade(score):
    if score >= 90 and score <= 100:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    elif score >= 0:
        print("F")
    else:
        print("Invalid Score")

grade(num)