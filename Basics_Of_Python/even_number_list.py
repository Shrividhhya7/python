number = [1,3,934,13,24,88,124]

def even_number():
    even_nums = []
    for num in number:
        if num % 2 == 0:
            even_nums.append(num)
    return even_nums
        
print(even_number())