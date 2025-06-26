def duplicates():
    input = [1, 2, 2, 3, 4, 4, 5]
    unique_number = []
    for i in input:
        if i not in unique_number:
            unique_number.append(i)
    return unique_number


print(duplicates())