def count_digits():
    n = int(input("Enter a number:" ))
    conv = str(abs(n))
    leng = len(conv)
    print(f"{n} has {leng} digits")

count_digits()