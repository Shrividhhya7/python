def sum_upto_n():
    num= int(input("Enter a Number: "))
    total =0
    for i in range (1, num+1):
        total += i
    print("Sum is :", total)


sum_upto_n()