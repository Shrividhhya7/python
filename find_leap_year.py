leap_year= int(input("Enter a Year: "))

def leapyear(output):
    output = leap_year % 4
    if output == 0:
        print(f"{leap_year} is a leap year")
    else:
        print(f"{leap_year} is not a leap year")

leapyear(leap_year)
